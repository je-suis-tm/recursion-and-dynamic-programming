
# coding: utf-8

# In[1]:


#fractal is one of the interesting topics in geometry
#it is usually described by a recursive function
#voila,here we are!
import matplotlib.pyplot as plt


# In[2]:


#initialize
x1=0
x2=3
y=0
bar_height=5
between_interval=10
n=6


# In[3]:


#cantor set is one of the simplest fractal shape
#at each iteration,we divide each bar into three equal parts 
#we remove the mid part from each bar and keep the rest
#this effectively creates a binary tree
#check the link below for more details on math
# https://www.math.stonybrook.edu/~scott/Book331/Cantor_sets.html
def cantor_set(x1,x2,y,n,
               bar_height=5,between_interval=10):
    
    #base case
    if n==0:
        return
    
    else:
        
        #viz the first 1/3 and the last 1/3 
        plt.fill_between([x1,x1+(x2-x1)/3],
                         [y-between_interval]*2,
                         [y-bar_height-between_interval]*2,)
        plt.fill_between([x2-(x2-x1)/3,x2],
                         [y-between_interval]*2,
                         [y-bar_height-between_interval]*2,)
        
        #recursion
        cantor_set(x1,x1+(x2-x1)/3,
                   y-between_interval,
                   n-1)        
        cantor_set(x2-(x2-x1)/3,x2,
                   y-between_interval,
                   n-1)


# In[4]:


#viz
#as n increases
#the bar gets too slim to be visible
ax=plt.figure(figsize=(10,10))
plt.fill_between([x1,x2],
                 [y]*2,
                 [y-bar_height]*2,)
cantor_set(x1,x2,y,n)
plt.axis('off')
plt.show()

