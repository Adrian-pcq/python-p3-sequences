#!/usr/bin/env python3

fib_list = []

def print_fibonacci(length):
    a=0
    b=1
    if length == 0:
        print(fib_list)
    elif length ==1:
        fib_list.append(0)
        print(fib_list)
    elif length == 2:
        fib_list.append(1)
        print(fib_list)    
    else:    
        for i in range(2,length):
            c=a+b
            a=b
            b=c
            fib_list.append(b)
        print(fib_list)
