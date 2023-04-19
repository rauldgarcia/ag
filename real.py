import numpy as np
import math
import random
import copy

eta=2
d=10
problema=1
precision=3
neval=0
inf=-10
sup=10

#inf=-5.12
#sup=5.12

#npoblacion=int(input('Ingrese el tamaño de la población:'))
npoblacion=20
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
        poblacion[bit]=round(random.randrange(inf,sup)+random.random(),precision)
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

def seleccionpadres(pob): 
    padres=[[i for i in range(2)]for j in range(npoblacion)] #crea matriz de largo de la poblacion
    
    for i in range(npoblacion):
        aleat1=random.randrange(0,npoblacion-1)
        aleat2=random.randrange(0,npoblacion-1)
        vp1=pob[aleat1][1]
        vp2=pob[aleat2][1]

        if vp1<vp2:
            padres[i][0]=pob[aleat1][0]

        elif vp1>vp2:
            padres[i][0]=pob[aleat2][0]

        else:
            choice=random.choice((aleat1,aleat2))
            padres[i][0]=pob[choice][0]
    
    return padres

def cruza(pad):
    shijos=[[k for k in range(2)]for l in range(npoblacion)] #crea una matriz de largo de los hijos
    for par in range(0,npoblacion-1,2):
        p1=pad[par][0]
        p2=pad[par+1][0]

        p=flip(pcruza) #volado si se cruzan o no

        if p==1:
            h1=copy.deepcopy(p1)
            h2=copy.deepcopy(p2)

            for elemento in range(d-1):
                pp1=h1[elemento]
                pp2=h2[elemento]

                u=np.random.rand()

                if u<=0.5:
                    bq=(2*u)**(1/(eta+1))

                else:
                    bq=(1/(2*(1-u)))**(1/(eta+1))

                #bl=(pp1+pp2-(2*inf))/abs(pp2-pp1)
                #bu=((2*sup)-pp1-pp2)/abs(pp2-pp1)

                h1[elemento]=round(0.5*(((1+bq)*pp1)+((1-bq)*pp2)),precision)
                h2[elemento]=round(0.5*(((1-bq)*pp1)+((1+bq)*pp2)),precision)

            shijos[par][0]=h1
            shijos[par+1][0]=h2

        else:
            shijos[par][0]=p1
            shijos[par+1][0]=p2

    return shijos

poblacion=[[i for i in range(2)]for j in range(npoblacion)] #crea matriz de largo de la poblacion
for individuo in range(npoblacion):
    poblacion[individuo][0]=crea()
    poblacion[individuo][1]=evalua(poblacion[individuo][0])

print(poblacion)

padres=seleccionpadres(poblacion)
print(padres)

hijos=cruza(padres)
print(hijos)

def muta(hijos):
    for individuo in range(npoblacion):
        p=flip(pmuta) #volado si se muta o no
        
        if p==1:
            cadena=hijos[individuo][0]
            ran=random.randrange(0,d)
            cadena[ran]=random.randrange(inf,sup)
            hijos[individuo][0]=cadena
            hijos[individuo][1]=evalua(hijos[individuo][0])
        
    return hijos

hijos=muta(hijos)
print(hijos)