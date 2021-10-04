
# coding: utf-8

# In[1]:


#fractal is one of the interesting topics in geometry
#it is usually described by a recursive function
#voila,here we are!
using Plots


# In[2]:


coordinates=[(0,0),(3,0),(3,-3),(0,-3)]


# In[3]:


function sierpiński_carpet(coordinates,lvl,fig,colour="black")
    
    #stop recursion
    if lvl==0
        
        return
        
    end
    
    #unpack coordinates
    #coordinates follow clockwise order
    topleft=coordinates[1];topright=coordinates[2]
    bottomright=coordinates[3];bottomleft=coordinates[4]
    
    #create new coordinates
    topleft_new=(topleft[1]+(topright[1]-topleft[1])/3,
                bottomleft[2]+(topleft[2]-bottomleft[2])/3*2)

    topright_new=(topleft[1]+(topright[1]-topleft[1])/3*2,
                bottomleft[2]+(topleft[2]-bottomleft[2])/3*2)

    bottomleft_new=(topleft[1]+(topright[1]-topleft[1])/3,
                bottomleft[2]+(topleft[2]-bottomleft[2])/3)

    bottomright_new=(topleft[1]+(topright[1]-topleft[1])/3*2,
                bottomleft[2]+(topleft[2]-bottomleft[2])/3)

    coordinates_new=[topleft_new,topright_new,
                     bottomright_new,bottomleft_new]
    
    #viz new coordinates
    for i in 2:length(coordinates_new)
        
        #use ! to add to the existing figure
        plot!([coordinates_new[i][1],coordinates_new[i-1][1]],
                 [coordinates_new[i][2],coordinates_new[i-1][2]],
                  color=colour,legend=false,grid=false,axis=false)
        
    end
    
    #julia doesnt allow index at -1 so i have to add one extra line
    plot!([coordinates_new[1][1],coordinates_new[end][1]],
        [coordinates_new[1][2],coordinates_new[end][2]],
        color=colour,legend=false,grid=false,axis=false)
    
    #recursive plot sub carpets following clockwise order
    sierpiński_carpet([topleft,(topleft_new[1],topleft[2]),
                       topleft_new,(topleft[1],topleft_new[2])],lvl-1,fig)
    
    sierpiński_carpet([(topleft_new[1],topleft[2]),
                       (topright_new[1],topright[2]),
                       topright_new,topleft_new],lvl-1,fig)
    
    sierpiński_carpet([(topright_new[1],topright[2]),topright,
                       (topright[1],topright_new[2]),topright_new],
                        lvl-1,fig)
    
    sierpiński_carpet([topright_new,(topright[1],topright_new[2]),
                       (bottomright[1],bottomright_new[2]),
                        bottomright_new],lvl-1,fig)
    
    sierpiński_carpet([bottomright_new,(bottomright[1],bottomright_new[2]),
                       bottomright,(bottomright_new[1],bottomright[2])],
                       lvl-1,fig)
    
    sierpiński_carpet([bottomleft_new,bottomright_new,
                       (bottomright_new[1],bottomright[2]),
                       (bottomleft_new[1],bottomleft[2])],lvl-1,fig)
    
    sierpiński_carpet([(topleft[1],bottomleft_new[2]),bottomleft_new,
                       (bottomleft_new[1],bottomleft[2]),bottomleft],
                        lvl-1,fig)
    
    sierpiński_carpet([(topleft[1],topleft_new[2]),topleft_new,
                       bottomleft_new,(topleft[1],bottomleft_new[2])],
                       lvl-1,fig)
    
end


# In[4]:


#annoying feature of julia
#plot wont show up in a loop unless i specify
fig=plot(legend=false,grid=false,axis=false,showaxis=false)

sierpiński_carpet(coordinates,4,fig)

fig

