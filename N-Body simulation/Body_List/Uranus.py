import numpy as np
from Particle import Particle
from astropy.time import Time
t = Time("2001-04-26 19:00:0.0", scale="tdb") #Time 7pm 26th of April 2001
from astropy.coordinates import get_body_barycentric_posvel
from spiceypy import sxform, mxvg
G=6.67408e-11

'''
This is a template to create a new body .
To add a new body first you need to get its initial conditions .
If the body is from this list : 
'sun','mercury','venus','earth','mars','jupiter','saturn','uranus','neptune','pluto'
it is already imported. 
If the body is not on this list then you can go to https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/ to learn how to import more bodies. 
'''
'''
Change "sun" To a string of the bodies name from the list above or imported bodies 
'''
pos, vel = get_body_barycentric_posvel("Uranus", t, ephemeris="jpl")

# make a "state vector" of positions and velocities (in metres and metres/second, respectively)
statevec = [
    pos.xyz[0].to("m").value,
    pos.xyz[1].to("m").value,
    pos.xyz[2].to("m").value,
    vel.xyz[0].to("m/s").value,
    vel.xyz[1].to("m/s").value,
    vel.xyz[2].to("m/s").value,
]
# get transformation matrix to the ecliptic (use time in Julian Days)
trans = sxform("J2000", "ECLIPJ2000", t.jd)
# transform state vector to ecliptic
statevececl = mxvg(trans, statevec, 6, 6)
# get positions and velocties
position = [statevececl[0], statevececl[1], statevececl[2]]
velocity = [statevececl[3], statevececl[4], statevececl[5]]
from poliastro import constants


'''
Change the variable in the next equation to m then lowercase of the bodies name also change GM_sun to GM_(The body that you are creating a file For).
Then change Sun to the name of whatever body you are creating in the Particle class and before the class also make mass equal to the m(The body that you are creating a file For)
from the equation before hand.
'''
muranus = (constants.GM_uranus / G).value
Uranus = Particle(
    position=np.array(position),
    velocity=np.array(velocity),
    acceleration=np.array([0, 0, 0]),
    name="Uranus",
    mass=muranus
)
'''
SAVE THE FILE as a new .py not overriding the template file save as The name of Body Then Go to the bodies.py file and add the body to the Bodies list as instructed
'''