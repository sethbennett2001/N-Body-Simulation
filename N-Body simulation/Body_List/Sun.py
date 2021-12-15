import numpy as np
from Particle import Particle
from astropy.time import Time
t = Time("2001-04-26 19:00:0.0", scale="tdb") #Time 7pm 26th of April 2001
from astropy.coordinates import get_body_barycentric_posvel
pos, vel = get_body_barycentric_posvel("sun", t, ephemeris="jpl")
from spiceypy import sxform, mxvg
G =6.67408e-11
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

msun = (constants.GM_sun / G).value
Sun = Particle(
    position=np.array(position),
    velocity=np.array(velocity),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass=msun
)
