# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
        
printit(10)

#   
