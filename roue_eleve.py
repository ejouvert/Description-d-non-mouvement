import matplotlib.pyplot as plt
import numpy as np

# Lecture des donnees du fichier txt
t, x, y = np.loadtxt('roue2.txt', unpack=True, usecols=(0, 1, 2), delimiter = '\t', skiprows = 2)
vx, vy, ax, ay = [], [], [], []

for i in range(1, len(x)-1) :
  vx.append((x[i+1]-x[i-1])/(t[i+1]-t[i-1]))
  vy.append((y[i+1]-y[i-1])/(t[i+1]-t[i-1]))



# Creation du graphique
plt.axis('equal')
plt.title('Trajectoire aimant')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.plot(x, y, color = 'green', label = 'Trajectoire', marker = '+')

for i in range(len(vx)) :
  plt.quiver(x[i+1], y[i+1], vx[i], vy[i], angles = "xy", scale_units = "xy", scale = 10, color = "blue")

#for i in range(len(ax)) :
  #plt.quiver(x[i+2], y[i+2], ax[i], ay[i], angles = "xy", scale_units = "xy", scale = 100, color = "blue")

# Fin de la creation du graphique
plt.legend()
plt.show()