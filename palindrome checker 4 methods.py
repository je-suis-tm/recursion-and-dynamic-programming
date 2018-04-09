# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 18:10:50 2018

@author: Administrator
"""
#check if a string is a palindrome
#reversing a string is extremely easy
#at first i was thinking about using pop function
#however, for an empty string, pop function is still functional
#it would not stop itself
#it would show errors of popping from empty list
#so i have to use the classic way, slicing
#each time we slice the final letter
#to remove the unnecessary marks, we have to use regular expression

import re

def f(n):
    #this is the base case, when string is empty
    #we just return empty
    if n=='':
        return n
    else:
        return n[-1]+f(n[:-1])
    
def check(n):
    #this part is the regular expression to get only characters
    #and format all of em into lower cases
    c1=re.findall('[a-zA-Z0-9]',n.lower())
    c2=re.findall('[a-zA-Z0-9]',(f(n)).lower())
    if c1==c2:
        return True
    else:
        return False
    
    
    
#alternatively, we can use deque
#we pop from both sides to see if they are equal
#if not return false
#note that the length of string could be an odd number
#we wanna make sure the pop should take action while length of deque is larger than 1

from collections import deque

def g(n):
    
    c=re.findall('[a-zA-Z0-9]',n.lower())
    de=deque(c)
    while len(de) >=1:
        if de.pop()!=de.popleft():
            return False
    return True


#or we can use non recursive slicing
def h(n):
    c=re.findall('[a-zA-Z0-9]',n.lower())
    if c[::-1]==c:
        return True
    else:
        return False
    
#or creating a new list
#using loop to append new list from old list s popped item
def i(n):
    c=re.findall('[a-zA-Z0-9]',n.lower())
    d=[]
    for i in range(len(c)):
        d.append(c.pop())
    c=re.findall('[a-zA-Z0-9]',n.lower())

    if d==c:
        return True
    else:
        return False
    


print(check('Evil is a deed as I live!'))
print(g('Evil is a deed as I live!'))
print(h('Evil is a deed as I live!'))
print(i('Evil is a deed as I live!'))
#for time and space complexity, python non recursive slicing wins