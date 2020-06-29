
# coding: utf-8

# In[1]:

#fractal is one of the interesting topics in geometry
#it is usually described by a recursive function
#voila,here we are!
import matplotlib.pyplot as plt


# In[2]:


coordinates=[(0,0),(3,0),(3,-3),(0,-3)]


# In[3]:


def sierpiński_carpet(coordinates,lvl,colour='k'):
    
    #stop recursion
    if lvl==0:
        return
    
    #unpack coordinates
    #coordinates follow clockwise order
    topleft=coordinates[0];topright=coordinates[1]
    bottomright=coordinates[2];bottomleft=coordinates[3]
    
    #create new coordinates
    topleft_new=(topleft[0]+(topright[0]-topleft[0])/3,
                bottomleft[1]+(topleft[1]-bottomleft[1])/3*2)

    topright_new=(topleft[0]+(topright[0]-topleft[0])/3*2,
                bottomleft[1]+(topleft[1]-bottomleft[1])/3*2)

    bottomleft_new=(topleft[0]+(topright[0]-topleft[0])/3,
                bottomleft[1]+(topleft[1]-bottomleft[1])/3)

    bottomright_new=(topleft[0]+(topright[0]-topleft[0])/3*2,
                bottomleft[1]+(topleft[1]-bottomleft[1])/3)

    coordinates_new=[topleft_new,topright_new,bottomright_new,bottomleft_new]
    
    #viz new coordinates
    for i in range(len(coordinates_new)):
        plt.plot([coordinates_new[i][0],coordinates_new[i-1][0]],
                 [coordinates_new[i][1],coordinates_new[i-1][1]],c=colour)
    
    #recursive plot sub carpets following clockwise order
    sierpiński_carpet([topleft,(topleft_new[0],topleft[1]),
                       topleft_new,(topleft[0],topleft_new[1])],lvl-1)
    
    sierpiński_carpet([(topleft_new[0],topleft[1]),(topright_new[0],topright[1]),
                       topright_new,topleft_new],lvl-1)
    
    sierpiński_carpet([(topright_new[0],topright[1]),topright,
                       (topright[0],topright_new[1]),topright_new],lvl-1)
    
    sierpiński_carpet([topright_new,(topright[0],topright_new[1]),
                       (bottomright[0],bottomright_new[1]),bottomright_new],lvl-1)
    
    sierpiński_carpet([bottomright_new,(bottomright[0],bottomright_new[1]),
                       bottomright,(bottomright_new[0],bottomright[1]),],lvl-1)
    
    sierpiński_carpet([bottomleft_new,bottomright_new,
                       (bottomright_new[0],bottomright[1]),
                       (bottomleft_new[0],bottomleft[1])],lvl-1)
    
    sierpiński_carpet([(topleft[0],bottomleft_new[1]),bottomleft_new,
                       (bottomleft_new[0],bottomleft[1]),bottomleft],lvl-1)
    
    sierpiński_carpet([(topleft[0],topleft_new[1]),topleft_new,
                       bottomleft_new,(topleft[0],bottomleft_new[1])],lvl-1)


# In[4]:


sierpiński_carpet(coordinates,4)


# In[5]:


#you can check turtle version at the following link
# https://www.geeksforgeeks.org/python-sierpinski-carpet/

