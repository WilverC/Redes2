import re
import threading as th
import math as m

def contarPalabra(lista_archivos, contador,numero_archivo,palabras_buscadas):
    palabras_a = 0
    palabras_b = 0
    palabras_c = 0
    palabras_d = 0
    palabras_e = 0
    
    for i in range(numero_archivo):
        nombre_archivo = numero_archivo[i] 
        archivo = open(nombre_archivo,"w")
        lineas = archivo.readlines()
        for ev in lineas: #Cuenta el numero de palabras totales y particulares
            palabra = re.findall("([a-z\']+)", ev.strip(), re.I)
            if palabra:
                contador += len(palabra)
            if palabra == "Palabra a":
                palabras_a += 1
            if palabra == "Palabra b":
                palabras_b += 1
            if palabra == "Palabra c":
                palabras_c += 1
            if palabra == "Palabra d":
                palabras_d += 1
            if palabra == "Palabra e":
                palabras_e += 1

        if contador > 1:
            print("El archivo tene "+ contador + " palabras")
        archivo.close()
    pass

num_hilos = 3
num_libros = 30
#division y residuo de libros vs hilos
div = m.floor(num_libros/num_hilos)
mod = num_libros % num_hilos

#lista de archivos y palabras 
archivos = ["Archivo 1","Archivo 2", "Archivo 3"]
palabras = ["Palabra1", "Palabra 2", "Palabra 3"]

# variable de reparticion de libros
ini = [0]
fin = list()
inifin = list()

#lista de hilos
hilos = list()

aux = 0
aux2 = 0
c = 0

#creacion de inicios
for i in range(num_hilos):
    if mod != 0:
        aux = aux2
        aux2 = aux2 + div + 1
        t = t1 = th.Thread(name = ("Hilo " + str(i)), target = contarPalabra, args=(archivos[aux:aux2],inifin,div,palabras))
        hilos.append(t)
        t.start()
        mod = mod - 1
    else:
        ini.append(ini[i] + div)

for t in hilos:
    t.join()
    
#creacion de finales
#for i in range(num_hilos-1):
#    fin.append(ini[i+1])

#fin.append(num_libros)

#union de inicio y final
for i in range(num_hilos):
    inifin.append([ini[i], fin[i]])

print(inifin)

#creacion de los hilos
"""


"""