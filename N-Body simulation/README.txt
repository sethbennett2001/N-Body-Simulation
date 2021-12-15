-Particle.py File is used to define classes used in all simulations also has 3 static methods which are all different
Numerical methods. Also can update gravitional acceleration between bodies and electrostatic forces between bodies.
the deafault method selcted is the Euler-Cromer.

-Simulation.py simulates as system of N-Bodies in the solar system and outputs updated positions using the Particle class uses update in gravitional forces.
The paramerters of this file can be changed for different tests example the Time steps used for each iteration, 
the lenght of time the simulation can run for and the mothod of numerical approximation can be changed each approximation is labeled with a number in the file.
Also imports files from bodies.py that contains a list of the bodies that want to be ran in the simulation. Outputs data in a .npy file which cam be named what ever that is required, 
but to use it in other files the data inputed needs to be altered to theis file name.

-Bodies.py and Body_list folder these files are used to create a list of classes using the Particle Class form a set time of intial conditions for objects in the solar system.
The bodies file improts all the files from the Body_List folder and adds them to a list of of intial condition class files of solar bodys from JPL and Astropy. 

-Body_Template.py is a template file that goes through the process to add a new body int o the simultaion and this file should not be overrided or added to the body list directly it is prley a template.    

-SimulationES.py uses same parameter imputs as the Simualtion.py but uses the interaction of charges ie elecotrostaticforces the file is set up with an example.
Outputs a data file like Simulation.py too .

-N-Bodies_Orbit_plotter.py plots all the position of the particle classes as simulated in Simulation.py from the saved .npy file and automaticlly plots all the bodies.
But by Add the names of the boies as a string list in to the body list file in simulation only these bodies will be plotted.

-ElecotrostaticinteractionsPlotter.py works them same way as the other plotter but is set up for the electrostatic simulation in SimulationES.py plot.

-Test_of_conservation.py takes the .npy file created in Simulation.py and looks at the conservation of kinetic energy and Linear momentum.

-Method Comparison is a file that takes differrent inputs of time steps and compares selected numericl methods and compare the selected numerical methods.





 
   


 