import numpy as np
import copy
from Particle import Particle
import os
from Bodies import Bodies
"""
This file is used to run and create .npy data files that can be used to analyse a system of intracting gravitational N-bodies.
"""   
#Set how long the simulation you want to run is for in years. 
Years =1
#Set the deltaT is seconds . It is currently set to 360 seconds which is a good value for the solar system simulation
DeltaT=360
#To set the Method make Method equal to 1(Euler),2(Cromer) or 3(Verlet) 
Method=1
Seconds=(Years*3.154e+7)
Numberofiterations= int (Seconds/DeltaT)
Data=[]
for i in range(Numberofiterations):   
    for j in Bodies :
        j.setMethod(Method)
        j.acceleration=[0,0,0]

        for t in Bodies:
            if j != t:
                j.updateGravitationalAcceleration(t)
        j.update(DeltaT)     
    time = i*DeltaT+ DeltaT
    Datafor1time=[time]
    if i%24 == 0:
        for t in range(len(Bodies)):
            Datafor1time.append(copy.deepcopy(Bodies[t]))
        Data.append(Datafor1time)  
print ('The Number of iterations in this simulation runnig was ',Numberofiterations) 
#The location of the file can be saved a what ever is desired but defaults to nbodysimulation.npy .
np.save("nbodysimulation.npy", Data, allow_pickle=True)
