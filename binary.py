import numpy as np
import math
import random

d=10
inf=-10
sup=10
#inf=-5.12
#sup=5.12
precision=3
npoblacion=4

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

def seleccionpadres(pob):
    menor=math.inf
    for p in range(npoblacion):
        pob[p][1]=pob[p][1]*-1
        if pob[p][1]<menor:
            menor=pob[p][1]
    
    menor=abs(menor)*2
    sumatoria=0
    for q in range(npoblacion):
        pob[q][2]=pob[q][1]+menor
        sumatoria+=pob[q][2]
    
    mu=sumatoria/npoblacion

    for r in range(npoblacion):
        pob[r][3]=pob[r][2]/mu

    padres=[] #crea matriz de largo de la poblacion
    ptr=random.random()
    sum=0
    for i in range(npoblacion-1):
        sum+=pob[i][3]
        f=True
        while f!=False:
            padres.append(pob[i])
            ptr+=1
            if sum<=ptr:
                f=False

    return(padres)

poblacion=[[i for i in range(4)]for j in range(npoblacion)] #crea matriz de largo de la poblacion
print(poblacion)
for individuo in range(npoblacion):
    poblacion[individuo][0]=crea()
    poblacion[individuo][1]=evalua(poblacion[individuo][0])

print(poblacion)

padres=seleccionpadres(poblacion)
print(padres)