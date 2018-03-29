#!/usr/bin/env python3
from multiprocessing import Process,Queue
# from queue import Queue
queue=Queue()


def f1():
    queue.put('hello ,shiyanlou')

def f2():
    data=queue.get()
    print(data)

def main():
    Process(target=f1).start()
    Process(target=f2).start()

if __name__=='__main__':
    main()