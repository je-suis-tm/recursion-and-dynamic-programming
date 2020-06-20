# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:22:38 2018

@author: Administrator
"""

#its also called levenshtein distance
#it can be done via recursion too
#the recursion version is much more elegant yet less efficient
# https://github.com/je-suis-tm/recursion/blob/master/edit%20distance%20recursion.py

#edit distance is to minimize the steps transforming one string to another
#the way to solve this problem is very similar is to knapsack
#assume we have two strings a and b
#we build a matrix len(a)*len(b)
#however,given lists start at index zero
#our matrix should be (len(a)+1)*(len(b)+1)

#there are three different ways to transform a string
#insert,delete and replace
#we can use any of them or combined
#lets take a look at the best case first
#assume string a is string b
#we dont need to do anything
#so 0 steps would be the answer
#for the worst case
#when string a has nothing in common with string b
#we would have to replace the whole string a
#the steps become the maximum step which is max(len(a),len(b))
#for general case,the number of steps would fall between the worst and the best case
#assume we are at mth letter of string a and nth letter string b
#if we wanna get the optimal steps of transforming string a to string b
#we have to make sure at each letter transformation
#a[:m] and b[:n] have reached their optimal status
#otherwise,we could always find another combination of insert,delete and replace
#to get a "real" optimal a[:m] and b[:n]
#it would make our string transformation not so optimal any more
#it is the same logic as the optimization of knapsack problem
#after we set our logic straight
#we would take a look at three different approaches
#lets take a look at insertion
#basically we need to insert nth letter from string b into string a at nth position
#the cumulated steps we have taken should be matrix[m][n-1]+1
#matrix[m][n-1] is the steps for a[:m] to b[:n]
#for delete,it is vice versa
#the cumulated steps we have taken should be matrix[m-1][n]+1
#for replacement,it is a lil bit tricky
#there are two scenarios
#if a[m]==b[n]
#it should be matrix[m-1][n-1]
#we dont need any replacement at all
#else,it should be matrix[m-1][n-1]+1
#we replace mth letter of string a with nth letter of string b
#after we managed to understand three different approaches
#we want to take the minimum number of steps among these three approaches
#throughout the iteration of different positions of both strings
#in the end,we would get the optimal steps to transform one string to another,YAY
def edit_distance(a,b):
    
    len_a=len(a)
    len_b=len(b)
    
    #this part is to create a matrix of len(a)*len(b)
    #as lists start at index 0
    #we get a matrix of (len(a)+1)*(len(b)+1) instead
    c=[[0]*(len_b+1) for i in range(len_a+1)]
    
    for j in range(len_a+1):
        c[j][0]=j
    for k in range(len_b+1):
        c[0][k]=k
    
    #we take iterations on both string a and b
    #next,we check if a[m]==b[n]
    #if yes,no replacement needed
    #if no,replacement needed
    #we take a minimum function to see which combination would give the minimum steps
    #eventually we got what we are after
    for l in range(1,len_a+1):
        for m in range(1,len_b+1):            
            if a[l-1]==b[m-1]:
                c[l][m]=min(c[l-1][m]+1,c[l][m-1]+1,c[l-1][m-1])
            else:
                c[l][m]=min(c[l-1][m]+1,c[l][m-1]+1,c[l-1][m-1]+1)
                
    return c[len_a][len_b]

print(edit_distance('baiseé','bas'))
