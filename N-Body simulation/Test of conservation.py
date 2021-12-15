from Particle import Particle
import numpy as np 
"""
This is the file that takes any .npy file that is produced by the Simulation.py file and can see what percentage the conservation of energy of the simulation ran is . 
That value is then follwed by the percentage change of the momentum of the simulation.
And the final value is the speed in which the whole simulation is moving .
"""


DataIn = np.load("nbodysimulation.npy", allow_pickle=True)
InitialTotalKE=0
for i in range(1,len(DataIn[0])):
    InitialTotalKE += DataIn[0][i].kineticEnergy()

TotalKE=0
for i in range(1,len(DataIn[0])):
    TotalKE += DataIn[-1][i].kineticEnergy()
ChangeinKE = InitialTotalKE-TotalKE
print('The change in momentum is' , (ChangeinKE/InitialTotalKE)*100 ,'%')

InitialTotalLM=0
for i in range(1,len(DataIn[0])):
    InitialTotalLM += (DataIn[0][i].mass)*(DataIn[0][i].velocity)
normInitialTotalLM = np.linalg.norm(InitialTotalLM)  

TotalLM=0
for i in range(1,len(DataIn[0])):
    TotalLM += (DataIn[-1][i].mass)*(DataIn[-1][i].velocity)
normTotalLM = np.linalg.norm(TotalLM)
ChangeinLM = normInitialTotalLM-normTotalLM
print('The change in momentum is' , ChangeinLM/normInitialTotalLM*100 ,'%')

Totalmass=0

for i in range(1,len(DataIn[0])):
    Totalmass += (DataIn[0][i].mass)
Speedofthecentreofmass= np.linalg.norm(InitialTotalLM)/Totalmass
print('The speed of the centre of mass is' , Speedofthecentreofmass , 'm/s')
