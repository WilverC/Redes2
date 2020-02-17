#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

//Variables globales
int num_of_threads = 4000;
int row = 160,col=160;
int** A;
int** B;
int** C;

//Funciones seriales
void read_mat(int col, int row);
void print_result();

//Funcion paralela
void *matmul(void* rank);

int main(int argc, char* argv[]){
  
  pthread_t tid[num_of_threads];
  int i, j; 
  long rank;

  A = malloc(row*sizeof(int*)); 
      for(i=0;i<row;i++)
        A[i]=malloc(col*sizeof(int));

  B = malloc(row*sizeof(int*)); 
      for(i=0;i<row;i++)
        B[i]=malloc(col*sizeof(int)); 
  
  C =  malloc(row*sizeof(int*)); 
      for(i=0;i<row;i++)
        C[i]=malloc(col*sizeof(int));

  //Lectura de matrices
  read_mat(col,row);
  
  //Creación de threads
  for (rank = 0; rank < num_of_threads; rank++)
     pthread_create(&tid[rank], NULL,matmul , (void*) rank);

  //Unión de threads
  for (rank = 0; rank < num_of_threads; rank++)
      pthread_join(tid[rank], NULL);

  //Impresión de resultado
  print_result();

  //Liberación de memoria
  free(A);
  free(B);
  free(C);

  // Fin de proceso padre
  pthread_exit(NULL);
  return 0;
}

//-------------------------------------------
// Función que va ejecutarse en cada thread
void *matmul(void* id_arg){
  int i,j,k;
  long  id = (long ) id_arg;
  int rows_per_thr = col/num_of_threads;
  int start_index = id*rows_per_thr;
  int final_index = (id+1)*rows_per_thr;

  for(i=start_index;i<final_index;i++){
   for(j=0;j<col;j++){
    for(k=0;k<row;k++){
      C[i][j] += A[i][k]*B[k][j]; 
    }
   }
  }
}
//--------------------------------------------
void read_mat(int col, int row){
  int i,j;

  
 printf(" Primera matriz: \n");
  for(i = 0; i < row; i++){
      for(j = 0; j < col; j++){
        A[i][j] = (rand()%4) + 1;
        printf("%d ",A[i][j]);
      }
      printf("\n ");
   }

  printf("\n Segunda matriz \n");

  for(i = 0; i < row; i++){
      for(j = 0; j < col; j++){
          B[i][j] = (rand()%4) + 1; 
          printf("%d ",B[i][j]);
       }
       printf("\n ");
   }
}

void print_result(){
  int i,j;
  printf("\n Matriz resultado: \n");
  for(i = 0; i < row; i++){
      for(j = 0; j < col; j++){ 
         printf("%d ",C[i][j]); 
       }
      printf("\n");
   }

}