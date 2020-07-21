
# coding: utf-8

# In[1]:


#coin change is a straight forward dynamic programming problem
#you are given one note and a set of coins of different values
#assuming you have infinite supply of coins of different values
#we need to compute different ways of making change
#the order of the coins doesnt matter in this case
#more details can be found in the following link
# https://www.geeksforgeeks.org/coin-change-dp-7/
#the script can also be done in dynamic programming
# https://github.com/je-suis-tm/recursion-and-dynamic-programming/blob/master/coin%20change%20dynamic%20programming.py


# In[2]:


#to solve this problem via recursion
#we divide one big problem into two sub problems
#the case where coin of η value is excluded in the solutions
#and the case where at least one coin of η value is included
def coin_change(num,choice):
    
    #base case
    if num==0:
        
        return 1
    
    #prevent stack overflow
    if num<0:
        
        return 0
    
    output=0
    
    #iterate through cases of exclusion
    for i in range(len(choice)):
        
        #case of inclusion
        include=coin_change(num-choice[i],choice)
        exclude=0
        
        #case of exclusion
        if i>=1:
            
            exclude=coin_change(num,choice[:i])            
        
        #two sub problems merge into a big one
        output=include+exclude
    
    return output


# In[3]:


coin_change(4,[1,2,3])

