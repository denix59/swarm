# Copyright Xavier Denimal aka denix59
# This piece of code is distributed under "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
from matplotlib.animation import FuncAnimation
# from matplotlib.animation import PillowWriter

#absolute minimum [0, 0] for Rastrigin function
Xmin = [0, 0]

#plot parameters
xmin, xmax, ymin, ymax, zmin, zmax, step = -1.5, 1.5, -1.5, 1.5, -2, 6, 100

#model parameters
w = 0.8
cmax = 0.2
particles_number = 20

#auxiliaries variables to plot function
x, y, z = 0, 0, 0

#variables for animate plot
#ax, p, v, g

#Rastrigin function absolute minimum coordonates
#otherwise calculate them depending of the target function
xabsmin, yabsmin = 0, 0

#target function
def f(x, y):
    #Rastrigin function
    n, A = 2, 0.8
    return A*n + (x**2 - A*np.cos(2*np.pi*x)) + (y**2 - A*np.cos(2*np.pi*y))

def plot_function(xmin, xmax, ymin, ymax, zmin, zmax, step):
    global x, y, z
    x, y = np.array(np.meshgrid(np.linspace(xmin, xmax, step), np.linspace(ymin, ymax, step)))
    z = f(x, y)
    plt.figure('rastrigin', figsize=(10, 10))
    ax = plt.axes(projection='3d')
    ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax), zlim=(zmin, zmax), xlabel='X', ylabel='Y', zlabel='Z')
    ax.contour(x, y, z, 10, offset=-2, colors='blue', alpha=0.5)
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=colormaps['plasma'])
    return

def setup_animate_plot():
    global ax, p, v, g
    fig = plt.figure('swarm')
    ax = plt.axes()
    img = ax.imshow(z, extent=[xmin, xmax, ymin, ymax], origin='lower', cmap=colormaps['plasma'], alpha=0.5)
    fig.colorbar(img, ax=ax)
    ax.plot([xabsmin], [yabsmin], marker='x', markersize=5, color="white")
    contours = ax.contour(x, y, z, 5, colors='blue', alpha=0.4)
    ax.clabel(contours, inline=True, fontsize=8, fmt="%.0f")
    p = ax.scatter(X[0], X[1], marker='o', color='lime', alpha=0.5)
    v = ax.quiver(X[0], X[1], V[0], V[1], color='green', width=0.005, angles='xy', scale_units='xy', scale=1)
    g = plt.scatter([G[0]], [G[1]], marker='D', s=100, color='red', alpha=0.4)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    return

def iterate(i):
    global V, X, P, Pz, G, Gz
    # Update params
    rd1, rd2 = np.random.rand(2)
    V = w * V + cmax * rd1 * (P - X) + cmax * rd2 * (np.reshape(G, (-1, 1)) - X)
    X = X + V
    Z = f(X[0], X[1])
    P[:, (Pz >= Z)] = X[:, (Pz >= Z)]
    Pz = np.minimum(Pz, Z)
    G = P[:, Pz.argmin()]
    Gz = Pz.min()
    #print("Valeur minimum trouvée par l'essaim à l'itération ", "{:02d}".format(i + 1), " : ", "{:.2f}".format(Gz), )
    return

def animate(i):
    global ax, p, v, g
    title = 'Itération numéro {:02d}'.format(i + 1)
    # Update params
    iterate(i)
    # Set picture
    ax.set_title(title)
    p.set_offsets(X.T)
    v.set_offsets(X.T)
    v.set_UVC(V[0], V[1])
    #g.set_offsets(np.reshape(G, (-1, 1)))
    g.set_offsets(G)
    return ax, p, v, g

#initialization
rng = np.random.default_rng()
#position vector (2-dimensions = particles_numberX2)
X = rng.random((2, particles_number)) * 1.5  - 1.5
#velocity vector (2-dimensions = particles_numberX2)
V = rng.random((2, particles_number)) * 0.1
#best particles positions coordinates (2-dimensions = particles_numberX2))
P = X
#function values for best positions (1-dimensions = particles_number)
Pz = f(X[0], X[1])
#global best position coordinates (2 dimensions = 1X2)
G = P[:, Pz.argmin()]
#function value for global best position (number)
Gz = Pz.min()

plot_function(xmin, xmax, ymin, ymax, zmin, zmax, step)
#writer = PillowWriter(fps=2)
anim = FuncAnimation(plt.figure('swarm', figsize=(9, 9)), animate, init_func=setup_animate_plot(), frames=list(range(1, 50)), interval=500, blit=False, repeat=False)
#anim.save("PSO.gif", writer=writer)
plt.show()

