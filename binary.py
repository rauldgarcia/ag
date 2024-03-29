import numpy as np
import math
import random
from random import shuffle
import copy

d=10
problema=0
precision=3
neval=0


while problema!=1 and problema!=2:
    problema=int(input('Ingrese el número de problema que quiere resolver (1 o 2):'))

if problema==1:
    inf=-10
    sup=10

if problema==2:
    inf=-5.12
    sup=5.12


l=int(math.log2(((sup-inf)*(10**precision)))+0.9)

npoblacion=int(input('Ingrese el tamaño de la población:'))
pcruza=float(input('Ingrese la probabilidad de cruza en decimal(ejemplo=0.5):'))
pmuta=float(input('Ingrese la probabilidad de muta en decimal(ejemplo=0.5):'))
generaciones=int(input('Ingrese el número de generaciones:'))
evaluaciones=npoblacion*generaciones

def flip(p):
    n=random.random()
    if n<=p:
        return 1
    else:
        return 0

def crea():
    poblacion=np.zeros((l*d))
    for bit in range(len(poblacion)):
           poblacion[bit]=flip(0.5)
    return poblacion

def evalua(chain):
    global neval
    neval+=1
    separada=np.reshape(chain,(d,l))
    ev=0
    for sub in range(d):
        cad=separada[sub]
        cadf=np.flip(cad)
        valor=0
        for ind in range(l):
            valor=valor+(cadf[ind]*(2**(ind)))
        xreal=inf+((valor*(sup-inf))/((2**l)-1))
        
        if problema==1:
            ev=ev+(xreal**2)

        if problema==2:    
            ev=ev+(((xreal**2)-(10*math.cos(2*math.pi*xreal))))

    if problema==2:
        ev=(10*d)+ev

    return(round(ev,precision))

def seleccionpadres(pob): #universal estocastica
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
    
    mu=(sumatoria/npoblacion)

    for r in range(npoblacion):
        pob[r][3]=pob[r][2]/mu

    padres=[] #crea matriz de largo de la poblacion
    ptr=random.random()
    sum=0
    for i in range(npoblacion):
        sum+=pob[i][3]
        f=True
        while f!=False:
            padres.append(pob[i])
            ptr+=1
            if sum<=ptr:
                f=False

    return(padres)

def cruza(pad): #cruza uniforme
    shijos=[[k for k in range(4)]for l in range(npoblacion)] #crea una matriz de largo de los hijos
    for par in range(0,npoblacion-1,2):
        p1=pad[par][0]
        p2=pad[par+1][0]

        p=flip(pcruza) #volado si se cruzan o no
        if p==1:
            h1=np.zeros((l*d))
            h2=np.zeros((l*d))

            for ele in range(len(p1)):
                cr=flip(0.5)
                if cr==1:
                    h1[ele]=p2[ele]
                    h2[ele]=p1[ele]

                else:
                    h1[ele]=p1[ele]
                    h2[ele]=p2[ele]

            shijos[par][0]=h1
            shijos[par+1][0]=h2

        else:
            shijos[par][0]=p1
            shijos[par+1][0]=p2

    return shijos

def muta(hi): #mutacion por reordenamiento
    for i in range(npoblacion):
        p=flip(pmuta)
        if p==1:
            r1=random.randint(0,l*d)
            r2=random.randint(0,l*d)
            ra=[r1,r2]
            ra.sort()
            cad=hi[i][0]
            cha=cad[ra[0]:ra[1]]
            chaflip=np.flip(cha)
            cad[ra[0]:ra[1]]=chaflip
            hi[i][0]=cad
            hi[i][1]=evalua(cad)

        else:
            hi[i][1]=evalua(hi[i][0])

    return hi

def imprime(chain):
    separada=np.reshape(chain,(d,l))
    imp=[]
    for sub in range(d):
        cad=separada[sub]
        cadf=np.flip(cad)
        valor=0
        for ind in range(l):
            valor=round(valor+(cadf[ind]*(2**(ind))),precision)
        xreal=round(inf+((valor*(sup-inf))/((2**l)-1)),precision)
        imp.append(xreal)

    return imp

best=float('inf')
poblacion=[[i for i in range(4)]for j in range(npoblacion)] #crea matriz de largo de la poblacion
for individuo in range(npoblacion):
    poblacion[individuo][0]=crea()
    poblacion[individuo][1]=evalua(poblacion[individuo][0])
    besta=poblacion[individuo][1]
    if besta<best:
        best=besta

vectorevaluaciones=np.array([[neval,best]])

while neval<evaluaciones:
    copia=copy.deepcopy(poblacion)
    padres=seleccionpadres(poblacion)

    hijos=cruza(padres)

    hijos=muta(hijos)

    copia.sort(key=lambda x:x[1]) #ordena la matriz de acuerdo a numero de ataques de menor a mayor
    hijos.sort(key=lambda x:x[1])

    #print(poblacion)
    #print(hijos)

    hijos[-1][0]=copia[0][0]
    hijos[-1][1]=copia[0][1]
    hijos.sort(key=lambda x:x[1])
    mejors=copy.deepcopy(hijos[0][0])
    mejorv=copy.deepcopy(hijos[0][1])
    print("Mejor solucion actual:")
    print(imprime(hijos[0][0]))
    print("Mejor valor actual:")
    print(mejorv)

    vectorevaluacionesac=np.array([[neval,hijos[0][1]]])
    vectorevaluaciones=np.append(vectorevaluaciones,vectorevaluacionesac,axis=0)

    poblacion=hijos
    shuffle(poblacion)

print("Mejor valor:")
print(mejorv)
print("La mejor solucion es:")
print(imprime(mejors))
#print(vectorevaluaciones)
np.savetxt('corrida.csv',vectorevaluaciones,delimiter=",")