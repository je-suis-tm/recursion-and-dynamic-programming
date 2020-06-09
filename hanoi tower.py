
# coding: utf-8

# In[1]:


#hanoi tower is the classic recursion
#the logic behind it is amazing
#rules can be seen from this website:
# https://en.wikipedia.org/wiki/Tower_of_Hanoi


# In[2]:


def hanoi(n,a,b,c):
    
    #rule states that each time we can only move one element
    #so when the recursion reaches to base case 1
    #we print the movement of elements from a to c
    if n==1:
        print(a,'-',c)
        return
    
    #for the general case
    #the first step is to move everything above the base case from column a to column b
    #note that we set print a to c when n reaches one
    #so in this case we reorder the function, replace c with column b where elements actually move towards
    hanoi(n-1,a,c,b)
    
    #the second step is to move the base case from column a to column c
    #we are only moving base case, thats why n=1
    hanoi(1,a,b,c)
    
    #final step would be move everything above base case from column b to column c
    hanoi(n-1,b,a,c)
    
    
# In[3]:


hanoi(4,'a','b','c')


# the best explanation should be
# https://www.python-course.eu/towers_of_hanoi.php

