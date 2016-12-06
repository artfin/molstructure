from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt

step = 0.04
maxval = 1.0
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

J = 50
I0 = 6021.073
Vm = 624.432
Vp = 224.433

theta, phi = np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi, 40)
THETA, PHI = np.meshgrid(theta, phi)
R = 1/(4 * I0) * (((np.sqrt(Vp + J**2 * (np.cos(THETA)) **2)) + np.sqrt(Vm + J**2 * 
	(np.cos(PHI))**2 * (np.sin(THETA))**2))**2 + J**2 * (np.sin(PHI))**2 * (np.sin(THETA))**2)

X = R * np.sin(THETA) * np.cos(PHI)
Y = R * np.sin(THETA) * np.sin(PHI)
Z = R * np.cos(THETA)

ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, color = "gray", linewidth = 0)
ax.set_zlim3d(-0.3, 0.3)

#plt.show()
plt.savefig("surface.png")