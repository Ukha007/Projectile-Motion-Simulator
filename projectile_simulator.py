try:
    import numpy as np
except ImportError:
    raise ImportError("not found")
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



# calculation for the physics values

def calculate_trajectory(angle, speed, gravity):
    
    angle_rad = np.radians(angle)
    velocityX = speed * np.cos(angle_rad)
    velocityY = speed * np.sin(angle_rad)

    # how long the object is in the air for:
    time_flight = velocityY * 2 / gravity


    # time steps from start point 0 to time of flight
    t = np.linspace(0, time_flight, 500)

    # x and y coords at each time step

    x = velocityX * t
    y = velocityY * t - 0.5 * gravity * t**2

    return x, y



# init values 
angle = 45 # angle in degrees
speed = 25 # launch speed in m/s
gravity = 9.81 # grav accel in m/s^2

#  draw trajectory
# graph window
fig, ax = plt.subplots(figsize = (10, 5))
# so there is room for the sliders
plt.subplots_adjust(bottom = 0.35)
    




# show the window
plt.show()