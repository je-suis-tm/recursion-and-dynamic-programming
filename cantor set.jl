
# coding: utf-8

# In[1]:


#fractal is one of the interesting topics in geometry
#it is usually described by a recursive function
#voila,here we are!
using Plots


# In[2]:


#initialize
x1=0
x2=3
y=0
bar_height=5
between_interval=10
n=6;


# In[3]:


#create rectangle shape
rectangle(w,h,x,y)=Shape(x.+[0,w,w,0],y.-[0,0,h,h])


# In[4]:


#cantor set is one of the simplest fractal shape
#at each iteration,we divide each bar into three equal parts 
#we remove the mid part from each bar and keep the rest
#this effectively creates a binary tree
#check the link below for more details on math
# https://www.math.stonybrook.edu/~scott/Book331/Cantor_sets.html
function cantor_set(x1,x2,y,n,
               bar_height=5,between_interval=10)
    
    #base case
    if n==0
        return
    
    else
        
        #viz the first 1/3 and the last 1/3 
        plot!(rectangle((x2-x1)/3,bar_height,x1,y-between_interval))
        plot!(rectangle((x2-x1)/3,bar_height,x2-(x2-x1)/3,y-between_interval))

        #recursion
        cantor_set(x1,x1+(x2-x1)/3,
                   y-between_interval,
                   n-1)        
        cantor_set(x2-(x2-x1)/3,x2,
                   y-between_interval,
                   n-1)
        
    end
    
end


# In[5]:


#viz
#as n increases
#the bar gets too slim to be visible
gr(size=(250,250))
fig=plot(legend=false,grid=false,axis=false,ticks=false)
plot!(rectangle((x2-x1),bar_height,x1,y))
cantor_set(x1,x2,y,n)
fig


