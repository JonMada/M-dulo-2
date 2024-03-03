#Construcción de una función aleatoria ponderada de ganar, perder, empatar 

import numpy as np #esto nos permitira realizar selecciones aleatorias

def loteria_ponderada(ponderaciones):
    container_list = [] #Creamos una lista vacía

    for (name, ponderación) in ponderaciones.items():
        for _ in range (ponderación):
            container_list.append(name)
    
    return np.random.choice(container_list)

ponderaciones = {
    'ganar' : 1,
    'empatar' : 2,
    'perder' : 5
}

print(loteria_ponderada(ponderaciones))