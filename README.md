# DevOps Lab 2021 winter/spring
## Homework #3 by Andrei Karpyza
### Main information about package

This package can be used to do system-state snapshots one time, or in cycle with some period.

Parameters, whose will be written to the output-file are:
- Overall CPU load
- Overall memory usage
- Overall virtual memory usage  
- IO information
- Network information

### Output formats:

- JSON
- Plain text

### Information to understand

Logging-cycle is placed into secondary thread, therefore you can start this thread, and continue to execute some commands in the main thread. It is possible because we have a cycle, the main time of which iteration takes sleep() command. So, when logging thread is sleeping, we can get the CPU-resource in our hands (take it to the main thread) and start to execute someting else.

As you can understand, here can be some problems with start and stop of the secondary thread, but the problems are solved, and you need only to understand three things:
- You can't run more then one secondary thread in one time (it isn't allowed by me programmatically);
- To start a thread you need to create class-instance and execute command 'start_threading_task()' from it with corresponding parameters;
- To stop the thread you need to execute command 'stop_threading_task()' without any arguments.

### Installation

To install the package you only need to clone this repository, go to the it's folder and run next command:
```
pip install .
```
It will install package to your python libraries, and you will be able to use an alias "snapshot" to start the logging-process.

To see help-page you need to execute:
```
snapshot --help
```
Here is this help-page:
```
usage: snapshot [-h] [-p P] [-t T] [-m M]

Arguments for sys-snapshooter

optional arguments:
  -h, --help  show this help message and exit
  -p P        Input here a priod between the snapshots. Default value is 300s
  -t T        Input here an output-type. Possible values are: JSON and text
  -m M        Input here directory, which will be checked and displayed by
              snapshooter
```

#### That's all, what I wanted to say to you about the package. I hope, it will be useful.