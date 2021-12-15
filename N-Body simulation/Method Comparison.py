import numpy as np 
from matplotlib import pyplot as plt
from Particle import Particle
import copy
import os
from Bodies import Bodies
#WARNING this code my take a long time to run if the DeltaT is  small and Length of test is high. 
#set An integer defining the Numerical  method to use: 1 is Euler-Forward,2 is Euler-Cromer, 3 is Verlet method. and place into list to test methods against each other.
What_Methods_to_test = [1,2,3]
#set a list of Different values of deltaT that you want to test.
What_deltaT_to_test = [60000,300000]
#set leght of time you want the test to take place for in years.
Lengthoftest= 5
#set a list of string names of which are the names of he bodies in which you want to  plot

Bodies_Showing= ['Venus']
for Methodrange in What_Methods_to_test:
    for DeltaTrange in What_deltaT_to_test:   
        Years =Lengthoftest
        DeltaT=DeltaTrange
        Method=Methodrange
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
            if i%2 == 0:
                for t in range(len(Bodies)):
                    Datafor1time.append(copy.deepcopy(Bodies[t]))
                Data.append(Datafor1time)
        if Methodrange == 1:
            mthd='Forward'
        elif Methodrange == 2 :
            mthd='Cromer'
        elif Methodrange == 3 :
            mthd='Verlet'  
        for planet in Bodies_Showing:
            
            # get the index of the current planet in the DataIn list
            planetindex = 1
            for body in Data[0][1:]:
                if body.name == planet:
                    break
                planetindex += 1
            # extract the x and y positions of the planets
            planetx = [np.linalg.norm(data[planetindex].position) for data in Data]
            Times = [data[0] for data in Data]
            # plot the data
            m,b = np.polyfit(Times,planetx,1)
            y=[]
            for u in range(len(Times)):
                y.append(m*Times[u]+b)
            
            plt.plot(Times,y,label=(body.name , DeltaTrange ,mthd , 'Gradient=', int(m) ) )
        Bodies = [Data[0][numb] for numb in range(1,len(Data[0])) ]
            



plt.xlabel('Time "s"')
plt.ylabel('Displacement from centre "m"')

plt.legend()

plt.show()