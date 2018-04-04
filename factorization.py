# -*- coding: utf-8 -*-

#global list is the key
#otherwise we will lose the list throughout iterations
global list
list=[]

def f(n):
    #using while function to stop the loop if n is smaller than 4 
    while int(n/2)>2:
        #the factor of n can not exceed the half of n
        #assuming 2 is one of the factors
        #so the range of factors we are gonna try starts from 2 to int(n/2+1)
        #int function to solve the odd number problem
        for i in range(2,int(n/2)+1):
            # the factorization process
            if n%i==0:
                list.append(i)
                return f(n/i)
            #break is to stop infinite loop for prime number
            #prime numbers larger than 4 cannot jump outta loop without break
        break
    
    list.append(int(n))
    # append the last factor
    #it could be n itself if n is a prime number
    #in that case there is only one element in the list
    #or it could be the last indivisible factor of n which is also a prime number
    if len(list)==1:
        print('%d is a prime number'%(n))

f(100000097)
print(list)
