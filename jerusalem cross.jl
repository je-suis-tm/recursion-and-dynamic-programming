
# coding: utf-8

# In[1]:


#fractal is one of the interesting topics in geometry
#it is usually described by a recursive function
#voila,here we are!
using Plots


# In[2]:


#create rectangle shape
rectangle(w,h,x,y)=Shape(x.+[0,w,w,0],y.-[0,0,h,h])

#compute euclidean distance
function euclidean_distance(point1,point2)
    return √((point1[1]-point2[1])^2+(point1[2]-point2[2])^2)
end


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
function jerusalem_cross(top_left,top_right,bottom_left,bottom_right,n)
        
    if n<=0
        return
    else
        
        #compute the width
        width=euclidean_distance(top_left,top_right) 
    
        #create the cross
        plot!(rectangle(width*(√(2)-1)^2,
                width*(1-2*((√(2)-1)^2)),
                top_left[1]+width*(√(2)-1),
                top_left[2]-width*(√(2)-1)^2),
                color="black")
        plot!(rectangle(width*(1-2*((√(2)-1)^2)),
                width*(√(2)-1)^2,        
                top_left[1]+width*(√(2)-1)^2,
                top_left[2]-width*(√(2)-1)),
                color="black")
        
        #top left corner recursion
        jerusalem_cross(top_left,(top_left[1]+width*(√(2)-1),top_left[2]),
                        (top_left[1],top_left[2]-width*(√(2)-1)),
                        (top_left[1]+width*(√(2)-1),
                        top_left[2]-width*(√(2)-1)),n-1)
        
        #top right corner recursion
        jerusalem_cross((top_right[1]-width*(√(2)-1),top_left[2]),top_right,
                        (top_right[1]-width*(√(2)-1),
                         top_left[2]-width*(√(2)-1)),
                        (top_right[1],top_left[2]-width*(√(2)-1)),n-1)
        
        #bottom left corner recursion
        jerusalem_cross((bottom_left[1],bottom_left[2]+width*(√(2)-1)),
                        (bottom_left[1]+width*(√(2)-1),
                         bottom_left[2]+width*(√(2)-1)),
                        bottom_left,
                        (bottom_left[1]+width*(√(2)-1),bottom_left[2]),n-1)
        
        #bottom right corner recursion
        jerusalem_cross((bottom_right[1]-width*(√(2)-1),
                         bottom_right[2]+width*(√(2)-1)),
                        (bottom_right[1],
                         bottom_right[2]+width*(√(2)-1)),
                        (bottom_right[1]-width*(√(2)-1),
                         bottom_right[2]),
                        bottom_right,n-1)
        
        #top mid corner recursion
        jerusalem_cross((top_left[1]+width*(√(2)-1),top_left[2]),
                        (top_right[1]-width*(√(2)-1),top_left[2]),
                        (top_left[1]+width*(√(2)-1),
                         top_left[2]-width*(√(2)-1)^2),
                        (top_right[1]-width*(√(2)-1),
                         top_left[2]-width*(√(2)-1)^2),n-2)  
        
        #bottom mid corner recursion
        jerusalem_cross((bottom_left[1]+width*(√(2)-1),
                         bottom_left[2]+width*(√(2)-1)^2),
                        (bottom_right[1]-width*(√(2)-1),
                         bottom_left[2]+width*(√(2)-1)^2),
                        (bottom_left[1]+width*(√(2)-1),
                         bottom_left[2]),
                        (bottom_right[1]-width*(√(2)-1),
                         bottom_left[2]),n-2)
        
        #left mid corner recursion
        jerusalem_cross((bottom_left[1],
                         top_left[2]-width*(√(2)-1)),
                        (bottom_left[1]+width*(√(2)-1)^2,
                         top_left[2]-width*(√(2)-1)),
                        (bottom_left[1],bottom_left[2]+width*(√(2)-1)),
                        (bottom_left[1]+width*(√(2)-1)^2,
                         bottom_left[2]+width*(√(2)-1)),n-2)
        
        #right mid corner recursion
        jerusalem_cross((bottom_right[1]-width*(√(2)-1)^2,
                         top_right[2]-width*(√(2)-1)),
                        (bottom_right[1],
                         top_right[2]-width*(√(2)-1)), 
                        (bottom_right[1]-width*(√(2)-1)^2,
                         bottom_right[2]+width*(√(2)-1)),
                        (bottom_right[1],bottom_right[2]+width*(√(2)-1)),
                        n-2)
        
    end
 
end


# In[4]:


#initialize
top_left=(0,0)
top_right=(1,0)
bottom_left=(0,-1)
bottom_right=(1,-1)
n=5;


# In[5]:


#viz
gr(size=(500,500))
fig=plot(legend=false,grid=false,axis=false,ticks=false,
    
    xlim=(top_left[1],top_right[1]),
    ylim=(bottom_right[2],top_right[2]))
jerusalem_cross(top_left,top_right,bottom_left,bottom_right,n)
fig


