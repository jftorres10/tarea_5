import numpy as np
import matplotlib.pyplot as plt
import random
import numpy


datos= np.genfromtxt('CircuitoRC.txt')
x_tiempo = datos[:,0]
y_carga = datos[:,1]

# basado en el repositorio de github del curso de metodos computacionales 

def likelihood(y_obs, y_model):
    chi_squared = sum((y_obs-y_model)**2)
    return chi_squared**0.5

def mi_modelo(x_tiempo, R, C):
    vo= 10.0 
    Qmax = vo*C
    return Qmax*(1.0 - np.exp(-x_tiempo/(R*C)))


# los valores inciales tentativos para R y C 
R= 7
C= 15


R_camino =[]  
C_camino= []
l_camino = []

R_camino.append(R)
C_camino.append(C)


y_carga_inicial = mi_modelo(x_tiempo, R_camino[0], C_camino[0])
l_camino.append(likelihood(y_carga, y_carga_inicial))

n_iter = 22001
for i in range (n_iter):
    R_nuevo=  np.random.normal(R_camino[i], 0.1) 
    C_nuevo = np.random.normal(C_camino[i], 0.1)

    y_carga_inicial = mi_modelo(x_tiempo, R_camino[i], C_camino[i])
    y_carga_nuevo = mi_modelo(x_tiempo,R_nuevo,C_nuevo)
    
    l_nuevo = likelihood(y_carga, y_carga_nuevo)
    l_init = likelihood(y_carga, y_carga_inicial)
    
    alpha = l_nuevo/l_init
    if(alpha<=1.0):
        R_camino.append(R_nuevo) 
        C_camino.append(C_nuevo) 
        l_camino.append(l_nuevo)
    else:
        beta = random.random()
        if(beta>=0.9):
        	R_camino.append(R_nuevo) 
        	C_camino.append(C_nuevo) 
      		l_camino.append(l_nuevo)
        else:
        	R_camino.append(R_nuevo) 
        	C_camino.append(C_nuevo) 
        	l_camino.append(l_nuevo)




plt.figure()
plt.scatter(R_camino,C_camino)
plt.savefig('distribucion.png')

plt.figure()
count, bins, ignored =plt.hist(R_camino, 20, normed=True)
plt.savefig('histogramaR.png')
plt.xlabel('tiempo')


plt.figure()
count, bins, ignored =plt.hist(C_camino, 20, normed=True)
plt.savefig('histogramaC.png')


max_likelihood_id = np.argmin(l_camino)
mejor_R = R_camino[max_likelihood_id]
mejor_C = C_camino[max_likelihood_id]

print mejor_R
print mejor_C
mejor = mi_modelo(x_tiempo,mejor_R,mejor_C)
plt.scatter( x_tiempo,y_carga)
plt.plot(x_tiempo,mejor, lw=2, color='r')
plt.xlabel('tiempo')
plt.ylabel('carga')
plt.title('R='+str(mejor_R) + ' C='+str(mejor_C) )
plt.xlabel('tiempo')
plt.ylabel('carga')
plt.title('R='+str(mejor_R) + ' C='+str(mejor_C) )
plt.savefig('modelo_Vs_datos.png')








