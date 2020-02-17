import re
import threading as th

def contarPalabra(lista_archivos, contador, numero_archivo, palabras_buscadas):
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
archivos = ["Archivo 1","Archivo 2", "Archivo 3"]
palabras = ["Palabra1", "Palabra 2", "Palabra 3"]
hilos = list()

for i range(num_hilos):
    t = t1 = th.Thread(name = ("Hilo ", i), target = contarPalabra, args=(archivos,c,num,palabras))
    hilos.append(t)
    t.start()

for t in hilos:
    t.join()