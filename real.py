import numpy as np
import math
import random

d=10
problema=1
precision=3
neval=0
inf=-10
sup=10

#inf=-5.12
#sup=5.12

#npoblacion=int(input('Ingrese el tamaño de la población:'))
npoblacion=100
#pcruza=float(input('Ingrese la probabilidad de cruza en decimal(ejemplo=0.5):'))
pcruza=0.9
#pmuta=float(input('Ingrese la probabilidad de muta en decimal(ejemplo=0.5):'))
pmuta=0.9
#evaluaciones=int(input('Ingrese el número de evaluaciones:'))
evaluaciones=50000

def flip(p):
    n=random.random()
    if n<p:
        return 1
    else:
        return 0

def crea():
    poblacion=np.zeros((d))
    for bit in range(d):
        poblacion[bit]=random.randrange(inf,sup)+random.random()
    return poblacion

def evalua(chain):
    global neval
    neval+=1
    ev=0
    for sub in range(d):
        valor=0
        
        if problema==1:
            ev=ev+(chain[sub]**2)

        if problema==2:    
            ev=round(ev+((chain[sub]**2-(10*math.cos(2*math.pi*chain[sub])))),precision)

    if problema==2:
        ev+=round(10*d,precision)

    return(round(ev,precision))

poblacion=[[i for i in range(4)]for j in range(npoblacion)] #crea matriz de largo de la poblacion
for individuo in range(npoblacion):
    poblacion[individuo][0]=crea()
    poblacion[individuo][1]=evalua(poblacion[individuo][0])

print(poblacion)

