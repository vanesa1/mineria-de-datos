#Mandar a llamar al csv(archivo donde estan guardados nuestros datos)
import csv
#Importar libreria math para poder hacer operaciones matematicas
import math
#Se declara y se abre el archivo de nuestros datos para nuestro ejemplo
f= open('DataSet.csv')
#Lee el archivo con los datos
lns=csv.reader(f) 

#lee la lista de conjunto de datos del archivo csv
dataset=list(lns)

#En estas lineas nos pide ingresar los datos del alumno
print ("Por favor ingrese los datos solicitados \n\n")
#print("Edad: ",end="")
#edad=int(input())
#print("Matricula: ",end="")
#cuatrimestre=int(input())
print("Promedio hasta el momento: ",end="")
promedio=int(input())
print("Materias reprobadas: ",end="")
reprobadas=int(input())
print("Numero de vecinos a considerar: ",end="")

#En esta linea nos dice que el valor de k (el cuel es el numero de vecino) deber ser entero
k=int(input())
#se inicializan las variables en 0
distancias=[0,0]
beca=[0,0]
contador=0

#
for i in dataset:
    dataset[contador][2]=int(dataset[contador][2])
    dataset[contador][3]=int(dataset[contador][3])
#    dataset[contador][4]=int(dataset[contador][4])
    if (contador<2):
        interna=((dataset[contador][2]-promedio)**2)+((dataset[contador][3]-reprobadas)**2)
        raiz=math.sqrt(interna)
        distancias[contador]=raiz
        beca[contador]=dataset[contador][4]
    else:
        interna=((dataset[contador][2]-promedio)**2)+((dataset[contador][3]-reprobadas)**2)
        raiz=math.sqrt(interna)
        distancias.append(raiz)
        beca.append(dataset[contador][4])
    contador+=1

i=0

distancias
while (i<contador):
    j=i
    while( j < contador):
        if (distancias[i]>distancias[j]):
            temp=distancias[i]
            distancias[i]=distancias[j]
            distancias[j]=temp
            temp=beca[i]
            beca[i]=beca[j]
            beca[j]=temp
        j=j+1
    i=i+1

cont1=0
cont2=0


for x in range(0,k):
    if(beca[x]==1):
        cont1=cont1+1
    else:
        cont2=cont2+1
    print(beca[x])
  
tiene=0
notiene=0
var=0
print("------------------------------------------------------")

if (beca[0] == "Beca"):
    tiene=tiene+1
else:
    notiene=notiene+1

if (beca[1] == "Beca"):
    tiene=tiene+1
else:
    notiene=notiene+1

if (beca[2] == "Beca"):
    tiene=tiene+1
else:
    notiene=notiene+1

if (beca[3] == "Beca"):
    tiene=tiene+1
else:
    notiene=notiene+1
    
if (beca[4] == "Beca"):
    tiene=tiene+1
else:
    notiene=notiene+1
    
    
if (tiene>notiene):
    print("Beca")
    