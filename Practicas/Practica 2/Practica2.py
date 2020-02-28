import re
import threading as th
import math as m
<<<<<<< HEAD

#variables globales

sem1 = th.Semaphore(1)
sem2 = th.Semaphore(0)
letras = ['\0','\0','\0','\0']
numeros = ['\0','\0','\0','\0']
ecritura = ["A","B","C","D"]
=======
semZC1 = th.Semaphore(4)
#semZC2 = th.Semaphore(1)
zcLetras = [" " ," "," "," "]
nzcNumeros = ['\0','\0','\0','\0']
tipoLetra = ['A', 'B', 'C', 'D', 'E']
tipoNumero = ['1', '2', '3', '4', '5']
>>>>>>> 0d082f3e9ccfb00229057369f2726c1c50ce36e8

# Funciones para los hilos

def productor(id):
<<<<<<< HEAD
    for i in range(3):
        sem1.acquire()
        print("Hola soy el hilo productor", id," ", global escritura[i])
        sem2.release()
    
=======
    letra = tipoLetra[id]
    numero = tipoNumero[id]
    print("Hola soy el hilo productor", id)
    aux = 0
    for i in range(5):
        while True:
            #print("iterando en productor: "+ str(i))
            aux += 1
            if(aux == 3):
                aux = 0
            if(zcLetras[aux].isspace()):
                semZC1.acquire()
                zcLetras[aux] = letra
                semZC1.release()
                break
        #print(zcLetras)
>>>>>>> 0d082f3e9ccfb00229057369f2726c1c50ce36e8
    pass
 

def consumidor(id):
<<<<<<< HEAD
    for i in range(3):
        sem2.acquire()
        print("Hola soy el hilo consumidor", id," ", str(i))
        sem1.release()
    
=======
    for i in range(5):
        #print("Iteración numero: "+ str(i))
        aux = 0
        while True:
            if(aux == 3):
                aux = 0
            if not(zcLetras[aux].isspace()):
                semZC1.acquire()
                letraR = zcLetras[aux]
                print("Consumidor "+str(id)+" consumiendo: ", letraR)
                zcLetras[aux] = " "
                semZC1.release()
                break
    print("Consumidor "+str(id)+" termino de consumir")
>>>>>>> 0d082f3e9ccfb00229057369f2726c1c50ce36e8
    pass

hilosC = []
hilosP = []

#Creación de hilos
for i in range(5):
    t = th.Thread(name = ("Hilo " + str(i)), target = productor, args=(i,))
    hilosC.append(t)
    t2 = th.Thread(name = ("Hilo " + str(i)), target = consumidor, args=(i,))
    hilosP.append(t2)
#Inicializacion de hilos
for i in range(5):
    p = hilosC[i]
    p.start()
    p2 = hilosP[i]
    p2.start()
#Finalización de hilos    
for i in range(5):
    p = hilosC[i]
    p.join()
    p2 = hilosP[i]
    p2.join()
    
