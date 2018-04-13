# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 17:06:21 2018

@author: terry.mai
"""
import datetime as dt

def row(n): 
    list=[] 
    if n==1: 
#base case
        return [1] 
    else: 
        for i in range(1,len(row(n-1))): 
#rolling sum all the values with 2 windows from the previous row 
#but we cannot include two boudary numbers 1 in this list 
            temp=row(n-1)[i]+row(n-1)[i-1] 
            list.append(temp) 
#append 1 for both front and rear of the list 
        list.insert(0,1) 
        list.append(1) 
          
    return list 
    
def printit(n): 
    for j in range(1,n+1): 
        print(row(j)) 
    return 
         
#---------------------

#introduce a global dictionary
#the function is basically the same as the previous one
#except we add one more if function
#to see if we can find pas[n] in dictionary
#if so, we return the output
#if not, we append it to dictionary for future use
global dict
dict={1:[1]}
def pas(n):
    if n in dict:
        return dict[n]
    else:
        list=[] 
        if n==1: 
#base case
            return dict[1] 
        else: 
            for i in range(1,len(row(n-1))): 
#rolling sum all the values with 2 windows from the previous row 
#but we cannot include two boudary numbers 1 in this list 
                temp=pas(n-1)[i]+pas(n-1)[i-1] 
                list.append(temp) 
#append 1 for both front and rear of the list 
        list.insert(0,1) 
        list.append(1) 
        dict[n]=list
          
        return dict[n]

def printit2(n): 
    for j in range(1,n+1): 
        print(pas(j)) 
    return 
        
    
#-----------------
#comparison between recursion with memory and without memory
#use datetime now to capture the time and take the difference    
def compare(n):
    t1=dt.datetime.now()
    printit(n)
    t2=dt.datetime.now()
    
    
    t3=dt.datetime.now()
    printit2(n)
    t4=dt.datetime.now()
    
    print('without memory:',t2-t1,'\nwith memory',t4-t3)
    return

compare(12)