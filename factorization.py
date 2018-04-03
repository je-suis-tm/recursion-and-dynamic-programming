# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:30:00 2018

@author: terry.mai
"""

global list
list=[]

def f(n):
    while int(n/2)>2:
        #to stop the loop if n is smaller than 4 
        for i in range(2,int(n/2)+1):
            #the largest factor can only be the half of n, assuming 2 is one of the factors
            if n%i==0:
                # the factorization process
                list.append(i)
                return f(n/i)
        break
    # to stop infinite loop for prime number
    list.append(int(n))
    # append the last factor
    if len(list)==1:
        print('%d is a prime number'%(n))

f(100000097)
print(list)