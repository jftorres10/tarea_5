import numpy as np
import matplotlib.pyplot as plt

datos= np.genfromtxt('Canal_ionico.txt')
datos_Iter= np.genfromtxt('datos.dat')

x = datos_Iter[-1,0]
y = datos_Iter[-1,1]
r = datos_Iter[-1, 2]

x_circulo =np.linspace(x-r, x+r, 100) 
y_ciruclo = (r**2-(x_circulo-x)**2)**0.5 + y 
y_ciruclo2 = -(r**2-(x_circulo-x)**2)**0.5 + y 
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')
ax.plot(x_circulo,y_ciruclo, c='blue')
ax.plot(x_circulo,y_ciruclo2, c = 'blue')
ax.plot(datos[:,0],datos[:,1], 'o')
ax.plot(datos_Iter[:,0],datos_Iter[:,1],'.', color = 'black')
plt.xlabel('x(A)')
plt.ylabel('y(A)')
plt.title(x  )


fig.savefig('radio_de_poro.png')

plt.figure()
plt.hist(datos_Iter[:,0], color = 'y')
plt.xlabel('valor x')
plt.ylabel('numero de repeticiones')
plt.savefig('histrogramax.png')

plt.figure()
plt.hist(datos_Iter[:,1], color = 'b')
plt.xlabel('valor y')
plt.ylabel('numero de repeticiones')
plt.savefig('histrogramay.png')

plt.figure()
plt.hist(datos_Iter[:,2], color = 'r')
plt.xlabel('valor r')
plt.ylabel('numero de repeticiones')
plt.savefig('histrogramar.png')



