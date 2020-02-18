Funcion listaDatos <- buscarPalabra(listaNombres)
	temp <- lista
	Para libro<-rInf Hasta rSup Hacer
		archivo <- listaNombres[i]
		lineas <- leerArchivo
		palabras <- separarLineas
		contadoresPalabras = 0
		contadorTotal = 0
		Para ev<-0 Hasta totalPalabras Hacer
			Si ev = palabraBuscada Entonces
			
			SiNo
				contadorPalabra = contadorPalabra + 1
			FinSi
			temp <- Contadores+contadorTotal
			datos_totales <- temp
		FinPara
	FinPara
FinFuncion

Algoritmo BuscapalabraHilos
	Leer numHilos
	div <- numLibros/numHilos
	modu <- num_libros MOD numHilos
	listaHilos <- lista
	aux <- 0
	aux <- 0
	Para i<-0 Hasta numHilos Hacer
		Si modu!=0 Entonces
			aux <- aux2
			aux2 <- aux2+div
			// Crear Hilo con el rango definido
			listaHilos <- hilo
		SiNo
			aux <- aux2
			aux2 <- aux2+div+1
			// Crear Hilo con el rango definido por aux
			modu <- modu-1
			listaHilos <- hilo
		FinSi
	FinPara
	// Iniciar hilos
	// Finalizar hilos, recibiendo conteo de palabras
	Escribir Resultado,total=res
FinAlgoritmo
