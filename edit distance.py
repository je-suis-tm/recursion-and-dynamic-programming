# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:22:38 2018

@author: Administrator
"""

def edit(a,b):
    len_a=len(a)
    len_b=len(b)
    
    c=[]
    for i in range(len_a+1):
        c.append([0]*(len_b+1))
        
    for j in range(len_a+1):
        c[j][0]=j
    
    for k in range(len_b+1):
        c[0][k]=k
        
    for l in range(1,len_a+1):
        for m in range(len_b+1):
            if a[l-1]==b[m-1]:
                c[l][m]=min(c[l-1][m]+1,c[l][m-1]+1,c[l-1][m-1])
            else:
                c[l][m]=min(c[l-1][m]+1,c[l][m-1]+1,c[l-1][m-1]+1)
                
    return c[len_a][len_b]

import random as rd


    
temp=rd.randint(1,20)
temp1=rd.randint(1,20)
alphabet='abcdefghijklmnopqrstuvwxyz'
temp2=''
temp3=''

for n in range(temp):
    temp2+=alphabet[rd.randint(0,25)]

for o in range(temp1):
    temp3+=alphabet[rd.randint(0,25)]




print(temp2,temp3)
print(edit(temp2,temp3))
