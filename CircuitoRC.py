import numpy as np
import matplotlib.pyplot as plt

datos= np.genfromtxt('CircuitoRC.txt')
x_tiempo = datos[:,0]
y_carga = datos[:,1]

def likelihood(y_obs, y_model):
    chi_squared = (1.0/2.0)*sum((y_obs-y_model)**2)
    return exp(-chi_squared)

def mi_modelo(x_tiempo, R, C):
    vo= 10.0 
    Qmax = vo*C
    return Qmax*(1.0 - np.exp(-x_tiempo/(R*C)))

  	R= 7
	C= 15


R_camino = empty((0)) #this is an empty list to keep all the steps
C_camino= empty((0))
l_camino = empty((0))

R_camino = append(R_camino, 10)
C_camino = append(C_camino, 11)


y_carga_inicial = mi_modelo(x_tiempo, R_camino[0], C_camino[0])
l_camino = append(l_camino, likelihood(y_carga, y_carga_inicial))

n_iter = 10000
for i in range (n_iter):
    R_nuevo=  np.random.normal(R_camino[i], 1.0) 
    C_nuevo = np.random.normal(C_camino[i], 1.0)

    y_carga_inicial = mi_modelo(x_tiempo, R_camino[i], C_camino[i])
    y_carga_nuevo = mi_modelo(x_tiempo,R,C)
    
    l_nuevo = likelihood(y_carga, y_carga_nuevo)
    l_init = likelihood(y_carga, y_carga_inicial)
    
    alpha = l_nuevo/l_init
    if(alpha>=1.0):
        R_camino  = append(R_camino,R_nuevo)
        C_camino  = append(C_camino,C_nuevo)
        l_camino = append(l_camino, l_nuevo)
    else:
        beta = random.random()
        if(beta<=alpha):
            R_camino  = append(R_camino,R_nuevo)
            C_camino  = append(C_camino,C_nuevo)
            l_camino = append(l_camino, l_nuevo)
        else:
            R_camino  = append(R_camino,R_nuevo)
            C_camino  = append(C_camino,C_nuevo)
            l_camino = append(l_camino, l_nuevo)






max_likelihood_id = argmax(l_camino)
mejor_R = R_camino[max_likelihood_id]
mejor_C = C_camino[max_likelihood_id]

print mejor_R
print mejor_C




mejor = mi_modelo(x_tiempo,mejor_R,mejor_C)
scatter( x_tiempo,y_carga)
plot(x_tiempo,mejor)
plt.xlabel('tiempo')
plt.ylabel('carga')
plt.savefig('modelo Vs datos.png')