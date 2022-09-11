---
tags: GIOS, OMSCS, C, FileIO
---

# C and Files

These notes were taken from "The Linux Programming Interface: Chapter 4: File I/O: The Universal I/O Model".

## Overview
Files are a great way to start talking about system calls in the Unix philosophy. Loads of things are designed on the file model. Honestly kind of insane that the first sample project in this course deals with sockets.

Files operate much in the same way as sockets
- You create a file descriptor, which is an integer
- You perform operations with that descriptor.
- You call `close()` on the descriptor. 

All system calls for performing I/O refer to open files using a "file descriptor", which is a non-negative integer. A "file descriptor" can refer to loads of things, not just files
- open files
- pipes
- FIFOs
- sockets
- terminals
- devices
- regular files?

Each process has its own unique set of file descriptors, which is why the integers are so small, and increment. Typically FD `0`, `1`, and `2` refer to `stdin`, `stdout`, and `stderr`. It's possible to redirect these FDs to each other. This can happen via the `freopen()` library function.

## `open()`

```c
#include <sys/stat.h>  
#include <fcntl.h>

int open(const char *pathname, int flags, ... /* mode_t mode */);
```

Returns an FD on success, -1 on error.

- `pathname` is the path to the file. This can be local or global
- `flags` is a bit mask that specifies the "access mode" for the file.
	- `O_RDONLY` Open the file for reading only
	- `O_WRONLY` Open the file for writing only
	- `O_RDWR` Open the file for both reading and writing
- `mode` specifies the permissions that should be placed on the file. This uses the `mode_t` data type, which is a fancy integer. Essentially this corresponds to the integer representation of `rwxrwxrwx`.

Mode Table:
| Constant  | Octal value | Permission bit |
| --------- | ----------- | -------------- |
| `S_ISUID` | `04000`     | Set-user-ID    |
| `S_ISGID` | `02000`     | Set-group-ID   |
| `S_ISVTX` | `01000`     | Sticky         |
| `S_IRUSR` | `0400`      | User-read      |
| `S_IWUSR` | `0200`      | User-write     |
| `S_IXUSR` | `0100`      | User-execute   |
| `S_IRGRP` | `040`       | Group-read     |
| `S_IWGRP` | `020`       | Group-write    |
| `S_IXGRP` | `010`       | Group-execute  |
| `S_IROTH` | `04`        | Other-read     |
| `S_IWOTH` | `02`        | Other-write    |
| `S_IXOTH` | `01`        | Other-execute  |

## `read()`
```c
include <unistd.h>  
  
ssize_t read(int fd, void *buffer, size_t count);
```

- `fd` is the file descriptor
- `buffer` is a place to store the data
- `count` specifies the maximum number of bytes to read.

Note that system calls do not allocate memory for buffers that are used to return info to the caller. We must pass a pointer to a previous allocated memory buffer of the correct size.

Library functions _can_ and _do_ allocate memory buffers. File I/O system calls don't.

`read()` returns the number of bytes actually read. `0` if an EOF is encountered. `-1` if an error is encountered. It can and does return fewer bytes than requested.

```c
#define MAX_READ 20  
char buffer[MAX_READ + 1];  

ssize_t numread;
if ((numread = read(STDIN_FILENO, buffer, MAX_READ)) == -1)  
    errExit("read");  

buffer[numread] = '\0';

printf("The input data was: %s\n", buffer)
```

`read()` does _not_ put a null byte (`'\0'`) at the end of the data in the buffer. You have to do that yourself. The size of the buffer should always be one more than the largest string we expect to read.

## `write()`

```c
#include <unistd.h>  
  
ssize_t write(int fd, const void *buffer, size_t count);
```

The arguments to `write()` are similar to those of `read()`.

- `fd` yep
- `buffer` should contain the data you want to write to the file
- `count` should say "how many bytes".

Returns the number of bytes written. This does not guarantee that all of the data is now in the file. The Kernel buffers file data to make programs more efficient.

## `close()`
```c
#include <unistd.h>

int close(int fd);
```

Closes an open file descriptor. This frees the FD number for reuse by the process. When a process terminates, all open FDs are automatically closed. Closing a file can fail.

```c
if (close(fd) < 0)  
    errExit("close");
```

## `lseek()`
```c
#include <unistd.h>  
  
off_t lseek(int fd, off_t offset, int whence);
```

For each open file, the kernel records a _file offset_, sometimes also called the _read-write offset_ or _pointer_. This is the location in the file at which the next `read()` or `write()` will commence. The file offset is expressed as an ordinal byte position relative to the start of the file. The first byte of the file is at offset 0. Subsequent read/write calls increment that offset. `lseek()` changes the offset.

- `fd` the descriptor
- `offset` specifies the offset in bytes. This can be positive or negative.
- `whence`
	- `SEEK_SET` go to `offset` from beginning of file.
	- `SEEK_CUR` go to `offset` from current file offset
	- `SEEK_END` go to `offset` from end of file. In this case, `offset` is interpreted with respect to the next byte after the last byte of a file.

Performing `curr = lseek(fd, 0, SEEK_CUR);` returns the current offset without changing it. Some other examples:

```c
/* Start of file */
lseek(fd, 0, SEEK_SET);
/* Next byte after the end of the file */
lseek(fd, 0, SEEK_END);
/* Last byte of file */
lseek(fd, -1, SEEK_END);
/* Ten bytes prior to current location */
lseek(fd, -10, SEEK_CUR);
/* 10001 bytes past last byte of file */
lseek(fd, 10000, SEEK_END);
```

Adjusting the current offset does not perform any I/O, just changes a value that the Kernel is keeping track of. Also you can't `lseek` a pipe, FIFO, socket, nor terminal.

The `l` in `lseek` means `long`, which refers to the offset's datatype.

