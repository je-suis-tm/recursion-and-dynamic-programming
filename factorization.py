# -*- coding: utf-8 -*-

#global list is the key
#otherwise we will lose the list throughout iterations
global factors
factors=[]

def f(n):
    
    global factors
    
    #negative and float should be excluded
    assert n>=0 and type(n)!=float,"negative or float is not allowed"
        
    #if n is smaller than 4 
    #prime number it is
    if n>4:
        
        #exclude 1 and itself
        #the largest factor of n can not exceed the half of n
        #because 2 is the smallest factor
        #the range of factors we are gonna try starts from 2 to int(n/2+1)
        #int function to solve the odd number problem
        for i in range(2,int(n/2)+1):
            
            #the factorization process
            if n%i==0:
                factors.append(i)
                
                #return is crucial
                #if the number is not a prime number
                #it will stop function from appending non-prime factors
                #the next few lines will be ignored
                return f(int(n/i))
    
    #append the last factor    
    #it could be n itself if n is a prime number
    #in that case there is only one element in the list
    #or it could be the last indivisible factor of n which is also a prime number
    factors.append(int(n))
    
    if len(factors)==1:
        print('%d is a prime number'%(n))
        factors=[]

f(100000097)
print(factors)
