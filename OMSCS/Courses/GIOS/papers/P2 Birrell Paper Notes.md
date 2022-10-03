---
tags: OMSCS, GIOS, Threads, PThreads
---
# Birrell Paper
Birrell's paper talks about how many operating systems already had support for multi-threaded processes, where multiple executing threads share a single address space, back in 1989. Multithreading was still pretty new back then, even experimental. Multi-processor CPUs were also pretty new. With respect to multithreaded programs, there were also a lot of common pitfalls, such as deadlocks and some more insidious performance issues.

The paper advocates for techniques that makes writing multithreaded programs easier, and demonstrates common "gotchas" and issues.

Properties of these threads
- each thread has its own call stack
- off-stack (i.e. heap) memory is shared "globally" among all threads
- require synchronization methods to ensure that "the correct answer is given"
- Thread creation/existence/destruction/synchronization primitives are all "lightweight" so the programmer should be able to use all of them freely

In this paper
- Birrell calls out his own biases with respect to the selection and implementation of issues and solutions
- Code samples are "written in Modula-2+"

> Threads are not a tool for automatic parallel decomposition, where a compiler will take a visibly sequential program and generate object code to utilize multiple processors. That is an entirely different art...

## Why Use Concurrency
- "The alternative, with most conventional operating systems, is to configure your program as multiple separate processes, running in separate address spaces. This tends to be expensive to set up, and the costs of communicating between address spaces are often high, even in the presence of shared segments. By using a lightweight multi-threading facility, the programmer can utilize the processors cheaply. This seems to work well in systems having up to about 10 processors, rather than 1000 processors."
- Hiding I/O latency
	- Waiting on user input
	- Waiting on the file system
	- This has benefits on CPUs that only support one thread of execution. (JavaScript has entered the chat)
- Distributed systems
	- Shared network servers (file servers, spooling print servers)
	- Multi threads means higher throughput
- Multi-threaded data structures
	- adding/removing entries from a balanced tree? Perform the rebalancing in a new thread. Gotta be crafty with mutex locking though

## Design of a Threading Library
- **Fork** creates threads
- **Join** waits for a thread to finish

```Modula-2+
VAR t: Thread;
t := Fork(a, x);
p := b(y);
q := Join(t);
```

- A **mutual-exclusion (mutex)** protects access to "critical sections" by `lock`-ing out all but one thread. That thread can then `unlock` the mutex once it's done preventing other threads from accessing a shared resource.
- **Condition variables** allow threads to `wait` until a condition is met, without burning a hole in the computer by spending 1000s of iterations checking a variable.
	- The `wait` will halt a thread (or many threads) until another thread calls `signal` or `broadcast`.
	- The condition variable is associated with a `mutex`. "The mutex associated with a condition variable protects the shared data that is used for the scheduling decision."
	- The mutex associated with a condition variable is typically expected to be `lock`-ed before calling `wait`. Calling `wait` on a condition will unlock the associated mutex.
	- Conditions are usually wrapped with a `while` loop
		- guards against waiting unnecessarily
		- guards against the thread continuing before the wait condition is actually met
- **Alerts** "is a mechanism for interrupting a particular thread, causing it to back out of some long-term wait or computation."
	- `alertwait` behaves the same as `wait`, except "if the thread’s alert-pending boolean is true, then instead of blocking on the condition, it sets alert-pending to false, re-locks the condition's associated mutex and raises an "Alerted" exception.
	- "If you call `Alert(t)` when `t` is currently blocked on a condition variable inside a call of `AlertWait` then `t` is awoken, `t` re-locks the mutex `m` and then it raises the exception `Alerted`."
	- If you call `Alert(t)` when `t` is not blocked in a call of `AlertWait`, all that happens is that its alert-pending boolean is set to true.
	- The call `TestAlert` atomically tests and clears the thread’s alert-pending boolean.

Birrell on what "Alerts" are good for

>For example, consider a “GetChar” routine, which blocks until a character is available on an interactive keyboard input stream. It seems attractive that if some other thread of the computation decides the input is no longer interesting (for example, the user clicked CANCEL with his mouse), then the thread should return from “GetChar”. If you happen to know the condition variable where “GetChar” blocks waiting for characters you could just signal it, but often that condition variable is hidden under one or more layers of abstraction. In this situation, the thread interpreting the CANCEL request can achieve its goal by calling “Thread.Alert(t)”, where “t” is the thread calling “GetChar”. For this to work, “GetChar” must contain something like the following fragment.

```Modula-2+
TRY
	WHILE empty DO Thread.AlertWait(m, nonEmpty) END;
	RETURN NextChar();
EXCEPT
	Thread.Alerted:
		RETURN EndOfFile;
END;
```

> Alerts are complicated, and their use produces complicated programs.

## Using Mutexes
> The basic rule for using mutual exclusion is straightforward: in a multi-threaded program all shared mutable data must be protected by associating it with some mutex, and you must access the data only from a thread that is holding the associated mutex.

Standard mutex stuff. Don't let 2 threads operate on 1 thing simultaneously, no matter how small. (Unless that thing advertises thread safety, in which case, it's doing its own mutex locking, so go ham.)

### Invariants
> When the data protected by a mutex is at all complicated, many programmers find it convenient to think of the mutex as protecting the invariant of the associated data. An invariant is a boolean function of the data that is true whenever the mutex is not held. So any thread that locks the mutex knows that it starts out with the invariant true. Each thread has the responsibility to restore the invariant before releasing the mutex

This boils down to including comments in your code which inform future developers as to which shared resources a mutex protects.

```C
mutex_t m1; // This mutex makes sure that only one thread can
            // access myheart at any given time.
humanbloodpump_t myheart;
```

### Cheating
Even changing the value of an integer could not be thread safe.

> Just Do It*
> 
> \- Nike
> 
> \* And by _it_ we mean "create a mutex and lock it even when your multithreaded program has multiple threads doing something simple like incrementing an integer."

### Deadlocks 
When you have more than one mutex, preserve the mutex lock order or your threads _will_ deadlock each other

- Thread A locks mutex M1;
- thread B locks mutex M2;
- thread A blocks trying to lock M2;
- thread B blocks trying to lock M1.

> Having your program deadlock is almost always a preferable risk to having your program give the wrong answer.

### Poor performance through lock conflicts
> Assuming that you have arranged your program to have enough mutexes that all the data is protected, and a fine enough granularity that it does not deadlock, the remaining mutex problems to worry about are all performance problems.

Don't let your threads hold mutexes longer than is necessary.
- Doing a DB transaction? Maybe save the network/file request for later? 
- Maybe don't try to acquire a 2nd mutex if necessary?

> In general, to get good performance you must arrange that lock conflicts are rare events. The best way to reduce lock conflicts is to lock at a finer granularity; but this introduces complexity. There is no way out of this dilemma—it is a trade-off inherent in concurrent computation.
> 
> The most typical example where locking granularity is important is in a module that manages a set of objects, for example a set of open buffered files. The simplest strategy is to use a single mutex for all the operations: open, close, read, write, and so forth. But this would prevent multiple writes on separate files proceeding in parallel, for no good reason. So a better strategy is to use one lock for operations on the global list of open files, and one lock per open file for operations affecting only that file. This can be achieved by associating a mutex with the record representing each open file.

There is effectively no limit to the number of mutexes your programs can use. Maximum performance may mean maximizing the number of mutexes.

Another performance issue comes up when threads of different priorities are able to lock the same mutex.

- Thread priorities
	- thread A is high priority
	- thread B is medium priority
	- thread C is low priority
- C is running (e.g. because A and B are blocked somewhere);
- C locks mutex M;
- B wakes up and pre-empts C
- (i.e. B runs instead of C since B has higher priority);
- B embarks on some very long computation;
- A wakes up and pre-empts B (since A has higher priority);
- A tries to lock M;
- A blocks, and so the processor is given back to B;
- B continues its very long computation.

> The real solution of this problem lies with the implementer of your threads facility. He must somehow communicate to the scheduler that since A is blocked on M, the thread holding M should be viewed as having at least as high a priority as A. Unfortunately, your implementer has probably failed to do this.

### Releasing the mutex within a LOCK clause
> There are times when you want to unlock the mutex in some region of program nested inside a LOCK clause.

You must exercise extra care if you take advantage of this.
- you must be sure that the operations are correctly bracketed, even in the presence of exceptions.
- you must be prepared for the fact that the state of the monitor’s data might have changed while you had the mutex unlocked

> I recommend that you don't do this.

## Using Condition Variables
> A condition variable is used when the programmer wants to schedule the way in which multiple threads access some shared resource, and the simple one-at-a-time mutual exclusion provided by mutexes is not sufficient.

You should wrap your condition variables with `while` loops **pretty much always**. Waking up from waiting on a condition variable **is not a guarantee** that the thread is in a state where it has useful data to operate on. Some other thread may have gotten to it first, for example. Another example, shoddy programming, spurious wakeups, etc.

### Using Broadcast
- signalling a condition wakes up one thread
- broadcast wakes up all threads that are waiting on that condition
	- Sometimes broadcast is just simpler to use when you don't really care about spurious wakeups
	- Sometimes multiple threads can operate non-redundantly on the data that one thread has just made available (such as readers/writer locking #ReaderWriterProblem)

### Spurious Wake-Ups
If a thread wakes up but then just ends up going back to sleep without accomplishing real work, that's a spurious wake up
- Threads using broadcast when signal would have been sufficient. Most of the threads just end up going back.
- Waking up a thread when the necessary condition wasn't actually met. This one can be fixed 

### Spurious lock conflicts
Waking up only to end up acquiring a different lock. Even if it's locked for just a second, that requires 2 scheduling operations to get it running again. To fix, make sure you're signaling after unlocking.

### Starvation
When thread locks and priorities mean that a low priority thread never gets scheduled.

In the readers/writer problem when there's sufficient load, a writer will never be able to make progress since there will always be an active reader.

It might be worth adding a counter to the system to keep track of "blocked writers", and implement some policy that prevents some minimum of blocked writers before preventing new readers.

There's no limit on how complex you can make your starvation prevention.

### Complexity
> Usually, I find that moving the call of “Signal” to beyond the end of the LOCK clause is easy and worth the trouble, and that the other performance enhancements are not worth making.
>
> But sometimes they are important, and you should only ignore them after explicitly considering whether they are required in your particular situation.

### Deadlock
> You can introduce deadlocks by using condition variables.

- Thread A acquires resource (1);
- Thread B acquires resource (2);
- Thread A wants (2), so it waits on (2)’s condition variable;
- Thread B wants (1), so it waits on (1)’s condition variable.

> Deadlocks such as this are not significantly different from the ones we discussed in connection with mutexes. You should arrange that there is a partial order on the resources managed with condition variables, and that each thread wishing to acquire multiple resources does so according to this order.
> 
> For example, you might decide that (1) is ordered before (2). Then thread B would not be permitted to try to acquire (1) while holding (2), so the deadlock would not occur

> Most often this problem occurs when you lock a mutex at one abstraction level of your program then call down to a lower level, which (unknown to the higher level) blocks.

☝ This can be known as the "nested monitor problem".

## Using Fork: Working in Parallel
### Pipelining
See [[P2L2 Threads and Concurrency]] for notes on the pipeline model.

### The impact of your environment
Evaluate your OSes handling of threads before shipping a multithreaded application to production, using that OS as a base.

This paper was from 1989. Linux is probably fine. Watch out for any new-fangled non-Linux kernels.

I wonder how TempleOS handles threading. Is it any good?

### Potential problems with adding threads
> If you have significantly more threads ready to run than there are processors, you will usually find that your performance degrades.

- thread schedulers are quite slow at making general re-scheduling decisions
- if your thread has to be put on a queue, and later swapped into a processor in place of some other thread, it will be more expensive.
- if you have lots of threads running they are more likely to conflict over mutexes or over the resources managed by your condition variables.
- Adding more "performance threads" than processors available may slow down your application. You **should** worry about the number of threads blocked waiting to acquire a mutex.
- Adding more "waiting for I/O" threads is probably fine regardless of the number of CPU cores. You **shouldn't** worry about the number of threads blocked waiting for a "wait" condition.
- Watch out for the performance penalties of creating and destroying threads often. It's more efficient than doing the same for processes, but the threading library has to create a whole new stack every time. You can reclaim some of that performance by keeping "thread corpses" around for reuse.

## Using Alert: Diverting the Flow of Control
(Page 28)

## Additional Techniques
### Hierarchy of Threads
This technique describes
- higher abstractions only call lower ones
- abstractions on the same level don't call each other
- all actions are initiated at the top level

Respecting this hierarchical ordering is applicable to threading too
- main daemon thread doesn't call higher abstractions
- worker threads don't try to alter the main daemon thread

Maintaining a partial order should prevent deadlocks when locking mutexes.

### Up-calls
> The alternative technique is known as “up-calls”.

See: `CLARK, D. The structuring of systems using up-calls. In Proceedings of the 10th Symposium on Operating System Principles (Dec. 1985), 171-180`

### Version stamps
This is for a MT program caching information in a shared read store. If 2 processes/threads grab a piece of data, operate on it, then store it back, the last one to make a change wins.

Implementing a "version" stamp on the data entity allows a higher process to ensure that a thread/process is returning a result based on the latest version of the data.

```json
{
	"name": "John",
	"version": 12
}
```

This is also how distributed systems can cache data across a distributed system. Something needs to be able to determine which data is the right copy.

### Work crews
You should use **thread pools** when parallelizing tasks. Spinning up a new thread any time you have a new task to do runs the risk of running out of .

This method involves creating a pool of threads that all wait for tasks to be added to a **shared queue** of tasks.
- Worker threads created by a main daemon thread.
- Worker threads now waiting for new tasks to be added to the queue.
- Daemon thread adds a task to the work queue and signals to one of the waiting threads.
- Worker threads guard the wait operation with a `while` loop
	- so they don't operate if they're woken up accidentally (potential for spurious wake ups, but protects against segfaults/NPE's)
	- so they don't re-enter the wait condition if/when they complete a task and there's already more tasks available.

See: `VANDEVOORDE, M. and ROBERTS, E. Workcrews: an abstraction for controlling parallelism. (Submitted for publication; copies available from Eric Roberts at SRC).`

## Building your Program
(Page 31)

## Concluding Remarks
> Writing concurrent programs has a reputation for being exotic and difficult. I believe it is neither. You need a system that provides you with good primitives and suitable libraries, you need a basic caution and carefulness, you need an armory of useful techniques, and you need to know of the common pitfalls. I hope that this paper has helped you towards sharing my belief.

## Appendix
- Some threading libraries probably allow you to specify timeouts on mutex locks, where your thread will run a different algorithm in the event it waits for a lock too long. This could have the added benefit of preventing deadlocks, but really, just fix your damn deadlock conditions. FFS. Log warnings if/when you use thread mutex lock timeouts
- Some threading libraries may allows a "wait" call to block a thread until signal/broadcast are called **at least N times.**