
# coding: utf-8

# In[1]:


#fractal is one of the interesting topics in geometry
#it is usually described by a recursive function
#voila,here we are!
using Plots


# In[2]:


function sierpiński_triangle(coordinates,lvl,fig,colour="black")
    
    #stop recursion
    if lvl==0
    
        return
    
    end
    
    #unpack coordinates
    #coordinates have to follow the order of left,mid,right
    left=coordinates[1];mid=coordinates[2];right=coordinates[3]
    
    #compute mid point for each line
    left_new=((mid[1]-left[1])/2+left[1],(mid[2]-left[2])/2+left[2])
    mid_new=((right[1]-left[1])/2+left[1],(right[2]-left[2])/2+left[2])
    right_new=((right[1]-mid[1])/2+mid[1],(mid[2]-right[2])/2+right[2])
    
    #create new coordinates
    coordinates_new=[left_new,mid_new,right_new]
    
    #viz coordinates
    for i in coordinates
        
        for j in coordinates
            
            if i!=j
                                
                #use ! to add to the existing figure
                plot!([i[1],j[1]],[i[2],j[2]],
                      color=colour,axis=false,
                      legend=false,grid=false)    
                
            end
            
        end
        
    end
    
    #recursive plot sub triangles
    sierpiński_triangle([left,left_new,mid_new],lvl-1,fig)
    sierpiński_triangle([left_new,mid,right_new],lvl-1,fig)
    sierpiński_triangle([mid_new,right_new,right],lvl-1,fig)
    
end


# In[3]:


#annoying feature of julia
#plot wont show up in a loop unless i specify
gr(size=(250,250))
fig=plot(legend=false,grid=false,axis=false,showaxis=false)
sierpiński_triangle([(0,0),(0.5,1),(1,0)],4,fig)
fig

