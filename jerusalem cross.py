
# coding: utf-8

# In[1]:


#fractal is one of the interesting topics in geometry
#it is usually described by a recursive function
#voila,here we are!
import matplotlib.pyplot as plt


# In[2]:


#compute euclidean distance
def euclidean_distance(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5


# In[3]:


#recursively plot jerusalem cross
#it kinda looks like flag of georgia (n=2)
#i mean the eurasian country not a yankee state
#i call it jerusalem cross but it is aka cross menger square,jerusalem square
#it is a 2d version of jerusalem cube
#a good reference to jerusalem cube
# https://robertdickau.com/jerusalemcube.html
#a good understanding of sierpiński carpet is helpful as well
# https://github.com/je-suis-tm/recursion-and-dynamic-programming/blob/master/sierpi%C5%84ski%20carpet.py
#do not confuse it with quadratic cross,which creates new crosses from the tips
# https://onlinemathtools.com/generate-quadratic-cross-fractal
#or fibonacci snowflakes,which is more like koch snowflake
# http://www.slabbe.org/Publications/2011-fibo-snowflakes.pdf
#or vicsek fractal,which is more similar to crosslet cross
# https://en.wikipedia.org/wiki/Vicsek_fractal
def jerusalem_cross(top_left,top_right,bottom_left,bottom_right,n):
        
    if n<=0:
        return
    else:
        
        #compute the length
        length=euclidean_distance(top_left,top_right) 
    
        #create the cross
        plt.fill_between(
            [top_left[0]+length*(2**0.5-1),top_right[0]-length*(2**0.5-1)],
            [bottom_left[1]+length*(2**0.5-1)**2,bottom_left[1]+length*(2**0.5-1)**2],
            [top_left[1]-length*(2**0.5-1)**2,top_left[1]-length*(2**0.5-1)**2],
            color='k')
        plt.fill_between(
            [top_left[0]+length*(2**0.5-1)**2,top_right[0]-length*(2**0.5-1)**2],
            [bottom_left[1]+length*(2**0.5-1),bottom_left[1]+length*(2**0.5-1)],
            [top_left[1]-length*(2**0.5-1),top_left[1]-length*(2**0.5-1)],
            color='k')
        
        #top left corner recursion
        jerusalem_cross(top_left,(top_left[0]+length*(2**0.5-1),top_left[1]),
                        (top_left[0],top_left[1]-length*(2**0.5-1)),
                        (top_left[0]+length*(2**0.5-1),
                        top_left[1]-length*(2**0.5-1)),n-1)
        
        #top right corner recursion
        jerusalem_cross((top_right[0]-length*(2**0.5-1),top_left[1]),top_right,
                        (top_right[0]-length*(2**0.5-1),
                         top_left[1]-length*(2**0.5-1)),
                        (top_right[0],top_left[1]-length*(2**0.5-1)),n-1)
        
        #bottom left corner recursion
        jerusalem_cross((bottom_left[0],bottom_left[1]+length*(2**0.5-1)),
                        (bottom_left[0]+length*(2**0.5-1),
                         bottom_left[1]+length*(2**0.5-1)),
                        bottom_left,
                        (bottom_left[0]+length*(2**0.5-1),bottom_left[1]),n-1)
        
        #bottom right corner recursion
        jerusalem_cross((bottom_right[0]-length*(2**0.5-1),
                         bottom_right[1]+length*(2**0.5-1)),
                        (bottom_right[0],
                         bottom_right[1]+length*(2**0.5-1)),
                        (bottom_right[0]-length*(2**0.5-1),
                         bottom_right[1]),
                        bottom_right,n-1)
        
        #top mid corner recursion
        jerusalem_cross((top_left[0]+length*(2**0.5-1),top_left[1]),
                        (top_right[0]-length*(2**0.5-1),top_left[1]),
                        (top_left[0]+length*(2**0.5-1),
                         top_left[1]-length*(2**0.5-1)**2),
                        (top_right[0]-length*(2**0.5-1),
                         top_left[1]-length*(2**0.5-1)**2),n-2)  
        
        #bottom mid corner recursion
        jerusalem_cross((bottom_left[0]+length*(2**0.5-1),
                         bottom_left[1]+length*(2**0.5-1)**2),
                        (bottom_right[0]-length*(2**0.5-1),
                         bottom_left[1]+length*(2**0.5-1)**2),
                        (bottom_left[0]+length*(2**0.5-1),
                         bottom_left[1]),
                        (bottom_right[0]-length*(2**0.5-1),
                         bottom_left[1]),n-2)
        
        #left mid corner recursion
        jerusalem_cross((bottom_left[0],
                         top_left[1]-length*(2**0.5-1)),
                        (bottom_left[0]+length*(2**0.5-1)**2,
                         top_left[1]-length*(2**0.5-1)),
                        (bottom_left[0],bottom_left[1]+length*(2**0.5-1)),
                        (bottom_left[0]+length*(2**0.5-1)**2,
                         bottom_left[1]+length*(2**0.5-1)),n-2)
        
        #right mid corner recursion
        jerusalem_cross((bottom_right[0]-length*(2**0.5-1)**2,
                         top_right[1]-length*(2**0.5-1)),
                        (bottom_right[0],
                         top_right[1]-length*(2**0.5-1)), 
                        (bottom_right[0]-length*(2**0.5-1)**2,
                         bottom_right[1]+length*(2**0.5-1)),
                        (bottom_right[0],bottom_right[1]+length*(2**0.5-1)),
                        n-2)


# In[4]:


#initialize
top_left=(0,0)
top_right=(1,0)
bottom_left=(0,-1)
bottom_right=(1,-1)
n=5


# In[5]:


#viz
ax=plt.figure(figsize=(10,10))
jerusalem_cross(top_left,top_right,bottom_left,bottom_right,n)
plt.xlim(top_left[0],top_right[0])
plt.ylim(bottom_right[1],top_left[1],)
plt.axis('off')
plt.show()

