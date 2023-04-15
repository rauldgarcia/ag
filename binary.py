import numpy as np
import math
import random

d=10
inf=-10
sup=10
#inf=-5.12
#sup=5.12
precision=3
npoblacion=2

l=int(math.log2(((sup-inf)*(10**precision))+0.9))

def flip(p):
    n=random.random()
    if n<p:
        return 1
    else:
        return 0

def crea():
    poblacion=np.zeros((l*d))
    for bit in range(len(poblacion)):
        if flip(0.5)==1:
            poblacion[bit]=1
    return poblacion

poblacion=[[i for i in range(2)]for j in range(npoblacion)] #crea matriz de largo de la poblacion
for individuo in range(npoblacion):
    poblacion[individuo][0]=crea()
    #agregar aqui llamada a evaluacion

print(poblacion)