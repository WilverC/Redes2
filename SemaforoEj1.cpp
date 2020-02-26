#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <vector>
using namespace std;

void* productor1(void *);
void* productor2(void *);
void* productor3(void *);
void* consumidor1(void *);
void* consumidor2(void *);

//Variables globales 
vector<char> vg;

//Semaforos
sem_t sp1;
sem_t sp2;
sem_t sp3;
sem_t sc1;
sem_t sc2;

int main(int argc, char** argv){
    pthread_t pr1;
    pthread_t pr2;
    pthread_t pr3;
    pthread_t co1;
    pthread_t co2;
    //Inicialización de semaforos
    if(sem_init(&sp1,0,1)||
       sem_init(&sp2,0,0)||
       sem_init(&sp3,0,0)||
       sem_init(&sc1,0,1)||
       sem_init(&sc2,0,0)){
           printf("Error al crear el semaforo\n");
		exit(-1);
    }

    //Inicialización de hilos
    pthread_create(&pr1, NULL, productor1, NULL);
    pthread_create(&pr2, NULL, productor2, NULL);
    pthread_create(&pr3, NULL, productor3, NULL);
    pthread_create(&co1, NULL, consumidor1, NULL);
    pthread_create(&co2, NULL, consumidor2, NULL);
    //Recepción de hilos
    pthread_join(pr1, NULL);
	pthread_join(pr2, NULL);
    pthread_join(pr3, NULL);
	pthread_join(co1, NULL);
    pthread_join(co2, NULL);
	


    //Destrucción de semaforos
    sem_destroy(&sp1);
    sem_destroy(&sp2);
    sem_destroy(&sp3);
    sem_destroy(&sc1);
    sem_destroy(&sc2);
    
    return 0;
}

void* productor1(void *){
//ASCII PARA NUMEROS 48 - 57
int v[10] = {48 ,49, 50, 51, 52, 53, 54, 55, 56, 57};
    for(int i=1; i<10; i++){
            //sem_wait(&t);
            //zonaCritica[i] = v[i];
            printf("\nproduciendo: %c", (char)v[i]);
            vg.push_back(v[i]);
            //sem_post(&t2);
        }
}
void* productor2(void *){
//ASCII PARA LETRAS 97 - 107
int v[10] = {97, 98, 99, 100, 101, 102, 103, 104, 105, 106};
    for(int i=1; i<10; i++){
            //sem_wait(&t);
            //secCrit = v[i];
            printf("\nproduciendo: %c", (char)v[i]); 
            vg.push_back(v[i]);
            //sem_post(&t2);
        }
}

void* productor3(void *){
//ASCII PARA SIMBOLOS 33 - 43
int v[10] = {33, 34, 35, 36, 37, 38, 39, 40, 41, 42};
    for(int i=1; i<10; i++){
            //sem_wait(&t);
            //secCrit = v[i];
            printf("\nproduciendo: %c", (char)v[i]);
            vg.push_back(v[i]);
            //sem_post(&t2);
        }
}

void* consumidor1(void *){
    printf("\nConsumidor 1");
}

void* consumidor2(void *){
    printf("\nConsumidor 2");
}