
# coding: utf-8

#this is a test on how recursion with memory reduces time complexity

#i need a global dictionary to do the memorization
#or i can change function fib(n) into fib(n,mem)
global mem
mem={1:1,2:1}
import datetime as dt

#fib(n) is recursion with memory
#everytime we do the calculation, we store it in the dictionary
#i denote the key as the n th fibonacci number
#the value as the number itself
#if we can find the key in dictionary
#we simply return the value
#if not, we append the dictionary then return the value
def fib(n):
    if n in mem:
        return mem[n]


    else:
        mem[n]=(fib(n-1)+fib(n-2))
        return mem[n]

#this is the fibonacci recursion function without memory
#it is basically algorithm 101 for any coding language
def f(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return f(n-1)+f(n-2)

#i calculate how long these two functions take
#print out the comparison
def compare(n):
    t1=dt.datetime.now()
    f(n)
    t2=dt.datetime.now()
    print('recursion: ',t2-t1)
    
    t1=dt.datetime.now()
    fib(n)
    t2=dt.datetime.now()
    print('recursion with memory: ',t2-t1)


compare(20)
