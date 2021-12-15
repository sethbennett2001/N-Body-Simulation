import numpy as np 
from matplotlib import pyplot as plt
from Particle import Particle
DataIn = np.load("nbodysimulation.npy", allow_pickle=True)
from Bodies import Bodies
"""
This file default Plots all the positions in space from the file created in Simulation.py . 
To Plot only certain bodies change the list of strings as instructed below .
"""



Body_Names=[]
for i in Bodies:
    Body_Names.append( i.name)
#if you want to only plot certian bodies in which the name sting of there class is known then a list of the strings can be add below insted of Body_Names.
for planet in Body_Names:
    # get the index of the current planet in the DataIn list
    planetindex = 1
    for body in DataIn[0][1:]:
        if body.name == planet:
            break
        planetindex += 1
    # extract the x and y positions of the planets
    planetx = [data[planetindex].position[0] for data in DataIn]
    planety = [data[planetindex].position[1] for data in DataIn]
    # plot the data
    plt.plot(planetx,planety,label=body.name)
plt.xlabel('Position in x "m"')
plt.ylabel('Position in y "m"')
plt.legend()
plt.show()
