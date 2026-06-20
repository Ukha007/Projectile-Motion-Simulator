try:
    import numpy as np
except ImportError:
    raise ImportError("not found")
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider





# init values 
angle = 45 # angle in degrees
speed = 25 # launch speed in m/s
gravity = 9.81 # grav accel in m/s^2

#  draw trajectory
# graph window
fig, ax = plt.subplots(figsize = (10, 5))
# so there is room for the sliders
plt.subplots_adjust(bottom = 0.35)


x, y = calculate_trajectory(angle, speed, gravity)
line = ax.plot(x, y, color = 'blue', linewidth = 2)

# labels for the axes on the graph
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Height (m)")
ax.set_title("Projectile Motion Sim")


# Sliders to control the sim









# show the window
plt.show()