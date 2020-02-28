import re
import threading as th
import math as m

#variables globales

sem1 = th.Semaphore(1)
sem2 = th.Semaphore(0)
letras = ['\0','\0','\0','\0']
numeros = ['\0','\0','\0','\0']
ecritura = ["A","B","C","D"]

# Funciones para los hilos

def productor(id):
    for i in range(3):
        sem1.acquire()
        print("Hola soy el hilo productor", id," ", global escritura[i])
        sem2.release()
    
    pass


def consumidor(id):
    for i in range(3):
        sem2.acquire()
        print("Hola soy el hilo consumidor", id," ", str(i))
        sem1.release()
    
    pass

hilosC = []
hilosP = []



for i in range(5):
    t = th.Thread(name = ("Hilo " + str(i)), target = productor, args=(i,))
    hilosC.append(t)
    t2 = th.Thread(name = ("Hilo " + str(i)), target = consumidor, args=(i,))
    hilosP.append(t2)
    
for i in range(5):
    p = hilosC[i]
    p.start()
    p2 = hilosP[i]
    p2.start()
    
for i in range(5):
    p = hilosC[i]
    p.join()
    p2 = hilosP[i]
    p2.join()