import re
import threading as th
import math as m

#variable global
datos_totales = list()

#funcion concurrente de conteo de palabras
def contarPalabra(lista_archivos): 
    temp = list()

    for libro in lista_archivos:    
        archivo = open(libro,"r", encoding="utf8")
        lineas = archivo.read()
        palabras = lineas.split()
        alegria = 0
        amor = 0
        enojo = 0
        ira = 0
        sueño = 0
        aburrimiento = 0
        contador = 0
        for ev in palabras: #Cuenta el numero de palabras totales y particulares
            ev.strip('\'\':;,.-*\"\"¿?¡!()').lower()
            contador += 1
            if ev == "alegria":
                alegria += 1
            if ev == "amor":
                amor += 1
            if ev == "enojo":
                enojo += 1
            if ev == "sueño":
                sueño += 1
            if ev == "ira":
                ira += 1
            if ev == "aburrimiento":
                aburrimiento += 1

        temp = [alegria, amor, enojo, ira, sueño, aburrimiento, contador]
        temp.append(libro)
        global datos_totales
        datos_totales.append(temp)
        archivo.close()
    
    pass


#Comienza el programa

#lista de archivos y palabras 
archivos = ["Cuentos\Cuento_1.txt",
            "Cuentos\Cuento_2.txt", 
            "Cuentos\Cuento_3.txt", 
            "Cuentos\Cuento_4.txt",
            "Cuentos\Cuento_5.txt",
            "Cuentos\Cuento_6.txt",
            "Cuentos\Cuento_7.txt",
            "Cuentos\Cuento_8.txt",
            "Cuentos\Cuento_9.txt",
            "Cuentos\Cuento_10.txt",
            "Cuentos\Cuento_11.txt",
            "Cuentos\Cuento_12.txt",
            "Cuentos\Cuento_13.txt",
            "Cuentos\Cuento_14.txt",
            "Cuentos\Cuento_15.txt",
            "Cuentos\Cuento_16.txt",
            "Cuentos\Cuento_17.txt",
            "Cuentos\Cuento_18.txt",
            "Cuentos\Cuento_19.txt",
            "Cuentos\Cuento_20.txt",
            "Cuentos\Cuento_21.txt",
            "Cuentos\Cuento_22.txt",
            "Cuentos\Cuento_23.txt",
            "Cuentos\Cuento_24.txt",
            "Cuentos\Cuento_25.txt",
            "Cuentos\Cuento_.txt"]

palabras = list()

#llamada a consola para numero de hilos
num_libros = len(archivos)
while 1:
    num_hilos = int(input("Introduce la cantidad de hilos: "))
    if(num_hilos <= num_libros):
        break
    else:
        print("No es necesario tantos hilos, se recomienda: ",num_libros)

#division y residuo de libros vs hilos
div = m.floor(num_libros/num_hilos)
mod = num_libros % num_hilos

#lista de hilos
hilos = list()

#creacion de los hilos
aux = 0
aux2 = 0
for i in range(num_hilos):
    if(mod != 0):
        aux = aux2
        aux2 = aux2 + div + 1
        t = th.Thread(name = ("Hilo " + str(i)), target = contarPalabra, args=(archivos[aux:aux2],))
        hilos.append(t)
        mod = mod - 1
    else:
        aux = aux2
        aux2 = aux2 + div
        t = th.Thread(name = ("Hilo " + str(i)), target = contarPalabra, args=(archivos[aux:aux2],))
        hilos.append(t)


for t in hilos:
    t.start()

for t in hilos:
    t.join()

print(datos_totales)

#variables para el promedio de todos
alegria = 0
amor = 0
enojo = 0
ira = 0
sueño = 0
aburrimiento = 0
contador = 0

#Muestreo de datos
for dato in datos_totales:
    print("---------------------------------------")
    print("Nombre: ", dato[7])
    print("Alegria: ", dato[0])
    print("Amor: ", dato[1])
    print("Enojo: ", dato[2])
    print("Ira: ", dato[3])
    print("Sueño: ", dato[4])
    print("Aburrimiento: ", dato[5])
    print("Total de palabras: ", dato[6])

#suma da las palabras
for dato in datos_totales:
    alegria = alegria + dato[0]
    amor = amor + dato[1]
    enojo = enojo + dato[2]
    ira = ira + dato[3]
    sueño = sueño + dato[4]
    aburrimiento = aburrimiento + dato[5]
    contador = contador + dato[6]
    
#muestreo del promedio
print("*********************************")
print("Promedio de palabras")
print("Alegria: ", alegria/num_libros)
print("Amor: ", amor/num_libros)
print("Enojo: ", enojo/num_libros)
print("Ira: ", ira/num_libros)
print("Sueño: ", sueño/num_libros)
print("Aburrimiento: ", aburrimiento/num_libros)
print("Total de palabras: ", contador/num_libros)