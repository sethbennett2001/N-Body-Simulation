import numpy as np
import copy
from Particle import Particle
import os
"""
This file is used to run and create .npy data files that can be used to analyse a system of intracting gravitational N-bodies.
"""   
Chargedparticle1 = Particle(
    position=np.array([1,0.1,0]),
    velocity=np.array([-0.5,0,0]),
    acceleration=np.array([0, 0, 0]),
    name="Particle1",
    mass=1,
    Charge=-0.000001
)
Chargedparticle2 = Particle(
    position=np.array([-1,-0.1,0]),
    velocity=np.array([0.5,0,0]),
    acceleration=np.array([0, 0, 0]),
    name="Particle2",
    mass=1,
    Charge=-0.000001
)

#Set how long the simulation you want to run is for in years. 
Seconds=5
#Set the deltaT is seconds . It is currently set to 360 seconds which is a good value for the solar system simulation
DeltaT=0.0001
#To set the Method make Method equal to 1(Euler),2(Cromer) or 3(Verlet) 
Method=2
Numberofiterations= int (Seconds/DeltaT)
Data=[]
Bodies=[Chargedparticle1,Chargedparticle2]
for i in range(Numberofiterations):   
    for j in Bodies :
        j.setMethod(Method)
        j.acceleration=[0,0,0]

        for t in Bodies:
            if j != t:
                j.updateElectrostaticAcceleration(t)
        j.update(DeltaT)     
    time = i*DeltaT+ DeltaT
    Datafor1time=[time]
    if i%1 == 0:
        for t in range(len(Bodies)):
            Datafor1time.append(copy.deepcopy(Bodies[t]))
        Data.append(Datafor1time)  
print ('The Number of iterations in this simulation runnig was ',Numberofiterations) 
#The location of the file can be saved a what ever is desired but defaults to nbodysimulation.npy .
np.save("nbodysimulationES.npy", Data, allow_pickle=True)