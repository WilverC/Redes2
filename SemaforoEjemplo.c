#include <stdio.h>
#include <stdlib.h>
//librearias importantes
#include <pthread.h>
#include <semaphore.h>

void* productor();
void* consumidor();

//global
int secCrit;
sem_t t;
sem_t t2;

int main(int argc, char *argv){
	pthread_t produc;
	pthread_t consu;
	int err,err2;
	int n;
	//Paso 1: Crear al semáforo
	err = sem_init(&t, 0, 1);
	if(err < 0){
		printf("Error al crear el semaforo\n");
		exit(-1);
	}

	err2 = sem_init(&t2, 0, 0);
	if(err2 < 0){
		printf("Error al crear el semaforo\n");
		exit(-1);
	}

	//Paso 2: Crear hilos
	pthread_create(&produc, NULL, (void*)productor, NULL);
	pthread_create(&consu, NULL, (void*)consumidor, NULL);


	pthread_join(produc, NULL);
	pthread_join(consu, NULL);

	//paso 5: destruir todo alv
	//solo en este caso :D
	sem_destroy(&t);
	sem_destroy(&t2);

	return 0;
}

// paso 3: contenido de las funciones
//paso 4: realizar las operaciones post y wait
// de acuerdo a la sincronacion que requerimos
void* productor(){
	for(int i=1; i<21; i++){
		sem_wait(&t);
		secCrit = i;
		printf("produciendo: %d\n", secCrit);
		sem_post(&t2);
	}
}

void* consumidor(){
	for (int i = 1; i < 21; i++)
	{
		sem_wait(&t2);
		printf("consumiendo: %d\n", secCrit);
		sem_post(&t);
	}
}


//se debe realizar 2 semaforos.