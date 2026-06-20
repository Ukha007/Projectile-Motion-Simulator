import numpy as np

# file for the physics calculations seperate to main file


# calculation for the physics values

def calculate_trajectory(angle, speed, gravity):
    #convert from degree to rad
    angle_rad = np.radians(angle)

    velocityX = speed * np.cos(angle_rad) #left/right
    velocityY = speed * np.sin(angle_rad) #up/down

    # how long the object is in the air for:
    time_flight = velocityY * 2 / gravity


    # time steps from start point 0 to time of flight
    t = np.linspace(0, time_flight, 500)

    # x and y coord positions at each time step
    x = velocityX * t
    y = velocityY * t - 0.5 * gravity * t**2

    return x, y
