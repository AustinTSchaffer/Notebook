---
tags: GIOS, OMSCS, C, Threads, PThreads
---

# Compiling Threaded C Programs

| Compiler / Platform  | Compiler Command        | Description         |
| -------------------- | ----------------------- | ------------------- |
| INTEL Linux          | `icc -pthread`          | C                   |
| INTEL Linux          | `icpc -pthread`         | C++                 |
| PGI Linux            | `pgcc -lpthread`        | C                   |
| PGI Linux            | `pgCC -lpthread`        | C++                 |
| GNU Linux, Blue Gene | `gcc -pthread`          | GNU C               |
| GNU Linux, Blue Gene | `g++ -pthread`          | GNU C++             |
| IBM Blue Gene        | `bgxlc_r` / `bgcc_r`    | C (ANSI / non-ANSI) |
| IBM Blue Gene        | `bgxlC_r` / `bgxlc++_r` | C++                 |
