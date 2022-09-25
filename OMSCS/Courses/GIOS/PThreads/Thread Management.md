---
tags: GIOS, OMSCS, C, Threads, PThreads
---
#  Thread Management

## Creating and Terminating Threads
https://hpc-tutorials.llnl.gov/posix/creating_and_terminating

```c
pthread_create(thread, attr, start_routine, arg)
pthread_exit(status)
pthread_cancel(thread)
pthread_attr_init(attr)
pthread_attr_destroy(attr)
```

### Creating Threads
Initially, a C program comprises a single, default thread. All other threads must be explicitly created by the program. `pthread_create` creates a new thread and make it executable. This routine can be called any number of times from anywhere within your code. Once created, threads are peers, and may create other threads.

`pthread_create` arguments:
- `thread`: An opaque pointer, unique identifier, or the new thread returned by the subroutine.
- `attr`: An opaque attribute object that may be used to set **thread attributes**. You can specify a thread attributes object, or `NULL` for the default values.
- `start_routine`: The C routine that the thread will execute on creation.
- `arg`: A single argument that may be passed to `start_routine`. It must be passed by reference as a pointer cast of type `void`. `NULL` may be used if no argument is to be passed.

Notes:
- There is no implied hierarchy or dependency between threads.
- There is a thread limit.

### Thread Attributes
Thread Attributes include:
- Detached or joinable state
- Scheduling inheritance
- Scheduling policy
- Scheduling parameters
- Scheduling contention scope
- Stack size
- Stack address
- Stack guard (overflow) size

`pthread_attr_init` and `pthread_attr_destroy` are used to initialize/destroy the thread attribute object.

### Thread Binding and Scheduling
After a thread has been created
- You do not know when it will be scheduled to run by the operating system
- You do not know which processor/core it will run on

[[The PThreads API]] provides several routines that may be used to specify how threads are scheduled for execution. For example, threads can be scheduled to run first-in first-out (**FIFO**), round-robin (**RR**) or **OTHER**, which allows the operating system to decide. It also provides the ability to set a thread’s scheduling priority value.

### Terminating Threads
There are several ways in which a thread may be terminated:

- The thread's starting routine *return*s.
- The thread makes a call to `pthread_exit`.
- The thread is canceled by another thread via `pthread_cancel`.
- The entire process is terminated due to making a call to either the `exec()` or `exit()`
- The main thread finishes.

`pthread_exit()`
- allows the programmer to specify an optional termination status. This optional parameter is typically returned to threads "joining" the terminated thread.
- does not close files or perform any other I/O cleanup. Any files opened inside the thread will remain open after the thread is terminated.
- If the main thread calls `pthread_exit()` as the last thing it does, the main thread will be kept alive to support the threads it created until they are done.

### Example Program

```c
#include <pthread.h>
#include <stdio.h>
#define NUM_THREADS     5

void *PrintHello(void *threadid)
{
  long tid;
  tid = (long)threadid;
  printf("Hello World! It's me, thread #%ld!\n", tid);
  pthread_exit(NULL);
}

int main (int argc, char *argv[])
{
  pthread_t threads[NUM_THREADS];
  int rc;
  long t;
  for(t=0; t<NUM_THREADS; t++){
    printf("In main: creating thread %ld\n", t);
    rc = pthread_create(&threads[t], NULL, PrintHello, (void *)t);
    if (rc) {
      printf("ERROR; return code from pthread_create() is %d\n", rc);
      exit(-1);
    }
  }

  /* Last thing that main() should do */
  pthread_exit(NULL);
}
```




## Passing Arguments to Threads
https://hpc-tutorials.llnl.gov/posix/passing_args/

`pthread_create()` can pass one argument to a thread's start routine. For cases where multiple arguments must be passed:
- create a structure which contains all of the arguments
- pass a pointer to `pthread_create()`

All arguments must be passed by reference and cast to `(void *)`.

Make sure that all data passed to a thread is thread safe, i.e. not modifiable after it is passed to the thread.

### Example of Integer Passing
```c
long taskids[NUM_THREADS];

for(t=0; t < NUM_THREADS; t++)
{
  taskids[t] = t;
  printf("Creating thread %ld\n", t);
  rc = pthread_create(&threads[t], NULL, PrintHello, (void *) taskids[t]);
  # ...
}
```

### Example of Struct Passing
An example of how to pass multiple arguments to a thread. Each thread receives a unique instance of the `thread_data` struct. Notice how the struct exists as statically allocated memory.

```c
struct thread_data{
  int  thread_id;
  int  sum;
  char *message;
};

struct thread_data thread_data_array[NUM_THREADS];

void *PrintHello(void *threadarg)
{
  struct thread_data *my_data;
  # ...
  my_data = (struct thread_data *) threadarg;
  taskid = my_data->thread_id;
  sum = my_data->sum;
  hello_msg = my_data->message;
  # ...
}

int main (int argc, char *argv[])
{
  # ...
  thread_data_array[t].thread_id = t;
  thread_data_array[t].sum = sum;
  thread_data_array[t].message = messages[t];
  rc = pthread_create(&threads[t], NULL, PrintHello, 
                      (void *) &thread_data_array[t]);
  # ...
}
```

Don't do this. `t` is shared memory space and visible to all threads. As the loop iterates, the value of this memory location changes, possibly before the created threads can access it.

```c
int rc;
long t;

for(t=0; t<NUM_THREADS; t++) 
{
   printf("Creating thread %ld\n", t);
   rc = pthread_create(&threads[t], NULL, PrintHello, (void *) &t);
   ...
}
```



## Joining and Detaching Threads
https://hpc-tutorials.llnl.gov/posix/joining_and_detaching/

TODO:

## Stack Management
https://hpc-tutorials.llnl.gov/posix/stack_management/

TODO:

## Miscellaneous
https://hpc-tutorials.llnl.gov/posix/misc_routines/

TODO: