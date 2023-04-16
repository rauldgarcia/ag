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

def evalua(chain):
    separada=np.reshape(chain,(d,l))
    ev=0
    for sub in range(d):
        cad=separada[sub]
        valor=0
        for ind in range(l):
            valor=valor+cad[ind]*(2**(l-1-ind))
        xreal=inf+((valor+(sup-inf))/((2**l)-1))
        ev=ev+(xreal**2)

    return(ev)

poblacion=[[i for i in range(2)]for j in range(npoblacion)] #crea matriz de largo de la poblacion
for individuo in range(npoblacion):
    poblacion[individuo][0]=crea()
    poblacion[individuo][1]=evalua(poblacion[individuo][0])

print(poblacion)