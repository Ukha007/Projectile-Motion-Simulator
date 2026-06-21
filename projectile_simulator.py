import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from physics import calculate_trajectory






# init values 
angle = 45 # angle in degrees
speed = 25 # launch speed in m/s
gravity = 9.81 # grav accel in m/s^2


# draw trajectory
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
graph.grid(True, linestyle='---', alpha=0.5)


# dotted trail line for the path of the ball as it moves
trail_line, = graph.plot([], [], color = 'blue', linewidth=2)
# ball (projectile) that moves along the path of the curve
ball_proj, = graph.plot([], [], 'o', color = 'red', markersize=0)



# Sliders to control the sim

#position and size for the slider
graph_angle = plt.axes([0.25, 0.22, 0.55, 0.03])
graph_speed = plt.axes([0.25, 0.15, 0.55, 0.03])
graph_gravity = plt.axes([0.25, 0.08, 0.55, 0.03])

# labels for the sliders 
slider_angle = Slider(graph_angle, 'Angle (∠∘)', 1, 89, valinit = angle)
slider_speed = Slider(graph_speed, 'Speed (m/s)', 1, 45, valinit = speed)
slider_gravity = Slider(graph_gravity, 'Gravity (m/s²)', 1, 25, valinit = gravity)

# Simulator start/reset buttons

graph_start = plt.axes([0.02, 0.20, 0.1, 0.05])
graph_reset = plt.axes([0.02, 0.09, 0.1, 0.05])


button_start = Button(graph_start, 'Start', color = 'blue')
button_reset = Button(graph_reset, 'Reset', color = 'red')



# animation logic for simulation that starts with the button presses

# store animation object for now
anim = None

def start_animation(event):
    global anim

    # stop any previous animation already running
    if anim is not None:
        anim.event_source.stop()

    # get current values for the slider
    current_angle = slider_angle.val
    current_speed = slider_speed.val
    current_gravity = slider_gravity.val

    #calculate the final trajectory
    x, y = calculate_trajectory(current_angle, current_speed, current_gravity)

    # scale the axis according to the scale of the trajectory

    window.set_xlim(0, max(x) * 1.5)
    window.set_ylim(0, max(y) * 1.5)


def animate(i):

    # i represents the current frame number, incrementing by the interval
    
    #drawing and updating the trail starting from the beginning frame
    trail_line.set_xdata(x[:i])
    trail_line.set_ydata(y[:i])

    # moving the ball to its current position and drawing it
    ball_proj.set_xdata(x[:i])
    ball_proj.set_ydata(y[:i])


    return trail_line, ball_proj

anim = animation.FuncAnimation(
    window,
    animate,
    frames=len(x), # how many steps per point in the trajectory
    interval=10, # milliseconds btwn the frames
    blit=True, # only redraw stuff that has changed
    repeat=False
)

window.canvas.draw_idle()


def reset(event):
    global anim

    #stop the animation logic if it is running
    if anim is not None:
        anim.event_source.stop()
    # clear the graph with empty brackets
    trail_line.set_xdata([])
    trail_line.set_ydata([])
    ball_proj.set_xdata([])
    ball_proj.set_ydata([])

    window.canvas.draw_idle()



button_start.on_clicked(animate)
button_reset.on_clicked(reset)
# display the window
plt.show()