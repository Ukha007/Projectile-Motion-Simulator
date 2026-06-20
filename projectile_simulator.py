try:
    import numpy as np
except ImportError:
    raise ImportError("not found")
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from physics import calculate_trajectory






# init values 
angle = 45 # angle in degrees
speed = 25 # launch speed in m/s
gravity = 9.81 # grav accel in m/s^2

#  draw trajectory
# graph window
window, graph = plt.subplots(figsize = (10, 5))
# so there is room for the sliders
plt.subplots_adjust(bottom = 0.35)


x, y = calculate_trajectory(angle, speed, gravity)
#colour for the curve
line, = graph.plot(x, y, color = 'blue', linewidth = 2)

# labels for the axes on the graph
graph.set_xlabel("Distance (m)")
graph.set_ylabel("Height (m)")
graph.set_title("Projectile Motion Sim")



# Sliders to control the sim

#position and size for the slider
graph_angle = plt.axes([0.15, 0.22, 0.55, 0.03])
graph_speed = plt.axes([0.15, 0.15, 0.55, 0.03])
graph_gravity = plt.axes([0.15, 0.08, 0.55, 0.03])

slider_angle = Slider(graph_angle, 'Angle (∠∘)', 1, 89, valinit = angle)
slider_speed = Slider(graph_speed, 'Speed (m/s)', 1, 45, valinit = speed)
slider_gravity = Slider(graph_gravity, 'Gravity (m/s^2)', 1, 25, valinit = gravity)










# show the window
plt.show()