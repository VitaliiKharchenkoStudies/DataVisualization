import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

r2d = np.linspace(0, 10, 100)
theta2d = np.linspace(0, 10 * np.pi, 100)

r3d = np.linspace(0, 10, 100)
theta3d = np.linspace(0, 10 * np.pi, 100)
z = np.linspace(0, 10, 100)

x2d = r2d * np.cos(theta2d)
y2d = r2d * np.sin(theta2d)
x3d = r3d * np.cos(theta3d)
y3d = r3d * np.sin(theta3d)

fig = plt.figure(figsize=(12, 6))

ax2d = fig.add_subplot(121)
ax2d.set_xlim(-12, 12)
ax2d.set_ylim(-12, 12)
circle2d, = ax2d.plot([], [], 'bo', ms=10)

ax3d = fig.add_subplot(122, projection='3d')
ax3d.set_xlim(-12, 12)
ax3d.set_ylim(-12, 12)
ax3d.set_zlim(0, 12)
sphere3d, = ax3d.plot([], [], 'bo', ms=10)


def init():
    circle2d.set_data([], [])
    sphere3d.set_data([], [])
    sphere3d.set_3d_properties([])
    return circle2d, sphere3d


def update(frame):
    circle2d.set_data([x2d[frame]], [y2d[frame]])
    sphere3d.set_data([x3d[frame]], [y3d[frame]])
    sphere3d.set_3d_properties([z[frame]])

    return circle2d, sphere3d


ani = FuncAnimation(fig, update, frames=len(x2d), init_func=init, blit=True)
ani.save('spiral_2d_3d_animation.gif', writer='pillow', fps=30)
plt.show()
