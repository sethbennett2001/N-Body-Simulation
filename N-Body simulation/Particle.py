import numpy as np

class Particle :
    """
    Class to setup an Body instance with an associated function.

    Parameters
    ----------
    position: array
        The position of the particle in 3 dimensions [x,y,z].
    velocity: array
        The velocity of the particle in 3 dimensions [x,y,z].
    acceleration: array
        The acceleration of the particle in 3 dimensions [x,y,z].

    name: string 
        A string that defines the name of the body.

    method: int
        An integer defining the Numerical  method to use: 1 is Euler-Forward,
        2 is Euler-Cromer, 3 is Verlet method. Default it to use the
        Euler-Cromer method.
    Charge: float
        A float number that defines the charge of the object.
    
    """
    
    def __init__(
        self,
        position=np.array([0, 0, 0], dtype=float),
        velocity=np.array([0, 0, 0], dtype=float),
        acceleration=np.array([0, 0, 0], dtype=float),
        name='Body',
        mass=1.0,
        G=6.67408e-11,
        Coulombsconstant=8.9875517923e9, 
        Charge=0,
        method=2
        
    
    ): 
        self.position=np.array(position, dtype=float)
        self.name = name
        self.mass = mass
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.G = G
        self.setMethod(method)
        self.Charge = Charge
        self.Coulombsconstant=Coulombsconstant

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
        self.name, self.mass,self.position, self.velocity, self.acceleration
        )
   
    def setMethod(self, method):
        if method == 1:
            self.Method = self.Euler
        elif method == 2:
            self.Method = self.Cromer
        elif method == 3:
            self.Method = self.Verlet
        else:
            raise ValueError(
                "Unrecognised method. Method must be 1 "
                "(Forward), 2 (Cromer), or 3 (Verlet)."
            )

    def update(self,deltaT):
        """
        Updates the Postion and Velocity For a time step deltaT

        Parameters
         ----------
         deltaT: (int, float)
            The time step of calculations.
        """

        
        x=self.Method(deltaT,self.position,self.velocity,self.acceleration,self.mass)
        self.position = x[0]
        self.velocity = x[1]
        
    
    def updateGravitationalAcceleration(self,body):
        """
        Updates the acceleration of the Class compared to another class
         Parameters
         ----------
         body: Class Particle
            Another Particle class in which the acceleration due to gravity is calculated.
        """
        
        TotalMagnitude = (((body.position[0]-self.position[0])**2)+((body.position[1]-self.position[1])**2)+((body.position[2]-self.position[2])**2))**(1/2)
        if TotalMagnitude != 0 :    
            self.acceleration += ((-self.G*body.mass)/((TotalMagnitude)**2))*((self.position-body.position)/(TotalMagnitude))
                         
    def updateElectrostaticAcceleration(self,body):
        """
        Updates the acceleration of the Class compared to another class
         Parameters
         ----------
         body: Class Particle
            Another Particle class in which the acceleration due to Electrostatics is calculated.
        """
        
        TotalMagnitude = (((body.position[0]-self.position[0])**2)+((body.position[1]-self.position[1])**2)+((body.position[2]-self.position[2])**2))**(1/2)
        if TotalMagnitude != 0 :    
            self.acceleration += (((self.Coulombsconstant*body.Charge*self.Charge)/((TotalMagnitude)**2))*((self.position-body.position)/(TotalMagnitude)))/self.mass

    def kineticEnergy(self):
        
        KE = 1/2*self.mass*(np.linalg.norm(self.velocity))**2  
        return KE 
    
    @staticmethod   
    def Euler(deltaT,position,velocity,acceleration,mass):
        """
        Euler-Forward method.

        Parameters
        ----------
        deltaT: (int, float)
            The lower bound of integral
        position: array
            The position of the particle in 3 dimensions [x,y,z].
        velocity: array
            The position of the particle in 3 dimensions [x,y,z]..
        acceleration: array
            The position of the particle in 3 dimensions [x,y,z].
        mass: (int, float)
            The function to be integrated.
        Return
        ------
        List:
            The updated postion and velocity.
        """
        
        
        newposition = position + (deltaT)*velocity
        
        newvelocity = velocity + (deltaT)*acceleration

        x=[newposition,newvelocity] 
        return x
        
    @staticmethod
    def Cromer(deltaT,position,velocity,acceleration,mass):
        """
        Euler-Cromer method.

        Parameters
        ----------
        deltaT: (int, float)
            The lower bound of integral
        position: array
            The position of the particle in 3 dimensions [x,y,z].
        velocity: array
            The position of the particle in 3 dimensions [x,y,z]..
        acceleration: array
            The position of the particle in 3 dimensions [x,y,z].
        mass: (int, float)
            The function to be integrated.
        Return
        ------
        List:
            The updated postion and velocity.
        """
        newvelocity = velocity + (deltaT)*acceleration
        
        newposition = position + (deltaT)*newvelocity
    
        x=[newposition,newvelocity] 
        return x
        


    @staticmethod
    def Verlet(deltaT,position,velocity,acceleration,mass):
        """
        Verlet method.

        Parameters
        ----------
        deltaT: (int, float)
            The lower bound of integral
        position: array
            The position of the particle in 3 dimensions [x,y,z].
        velocity: array
            The position of the particle in 3 dimensions [x,y,z]..
        acceleration: array
            The position of the particle in 3 dimensions [x,y,z].
        mass: (int, float)
            The function to be integrated.
        Return
        ------
        List:
            The updated postion and velocity.
        """

        newposition = position + (deltaT)*velocity + 1/2*acceleration*(deltaT)**2

        
        newvelocity1 = velocity + (1/2)*(deltaT)*acceleration

        newvelocity2 = newvelocity1 + (3/2)*(deltaT)*acceleration

        acceleartionplus = (newvelocity2-newvelocity1)/(deltaT) 

        newvelocity = velocity + (1/2)*(deltaT)*(acceleration+acceleartionplus)
        
        x=[newposition,newvelocity] 
        return x
        

