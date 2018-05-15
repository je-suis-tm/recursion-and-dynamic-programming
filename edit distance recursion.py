# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:22:38 2018

@author: Administrator
"""

def f(a,b):
    
    if a=='' or b=='':
        return max(len(a),len(b))
  
    temp=0 if a[-1]==b[-1] else 1
    steps=min(f(a[:-1],b)+1,f(a,b[:-1])+1,f(a[:-1],b[:-1])+temp)
    return steps

print(f('arsehole','asshoe'))