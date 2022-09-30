/* PThread Creation Quiz 3 */ 

#include <stdio.h>
#include <pthread.h>

#define NUM_THREADS 4

void *threadFunc(void *pArg) { /* thread main */
	int myNum = *((int*)pArg);
	printf("Thread number %d\n", myNum);
	return 0;
}

int main(void) {

	int i;
	int tNum[NUM_THREADS];
	pthread_t tid[NUM_THREADS];
	
	for(i = 0; i < NUM_THREADS; i++) { /* create/fork threads */
		tNum[i] = i;
		pthread_create(&tid[i], NULL, threadFunc, &tNum[i]);
	}
	
	for(i = 0; i < NUM_THREADS; i++) { /* wait/join threads */
		pthread_join(tid[i], NULL);
	}

	return 0;
}
