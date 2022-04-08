#!/usr/bin/env julia
# coding: utf-8

# In[1]:


#egg drop is a simple dynamic programming problem
#the player is given some number of eggs 
#to test eggs break by free fall from which floor
#more details can be found in the link below
# https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/


# In[2]:


#initialize
num_of_floors=271
num_of_eggs=3;


# In[3]:


#to solve this problem via dp
#we test all the floor with the eggs
function egg_drop(num_of_floors,num_of_eggs)

    #create tabulation matrix
    tabulation=[[NaN for _ in 1:num_of_floors] for _ in 1:num_of_eggs]

    #when u got one egg the number of attempts will always be the number of floors
    tabulation[1]=[ii for ii in 1:num_of_floors]

    #ground floor doesnt break eggs as its on the ground
    #first floor only takes one attempt no matter how many eggs we have
    for i in 2:num_of_eggs
        tabulation[i][1]=1
    end

    #since we initialize the ground floor and the first floor
    #the loop starts from 2
    for id_egg in 2:num_of_eggs
        for id_floor in 2:num_of_floors

            #at the current position (id_egg,id_floor)
            #there are id_egg number of eggs and id_floor number of floors
            #we start to experiment the worst case via brute force
            #we drop eggs on each floor
            #there are id_floor*2 scenarios        
            #each floor can be the one that breaks the egg or doesnt break the eggs
            #hence we compute how many trials are required for each scenario
            #take the maximum first to obtain worst case for each floor
            #and take the minimum to obtain the minimum number of trials
            tabulation[id_egg][id_floor]=minimum(
                append!([1+max(
                    tabulation[id_egg-1][j-1],
                    tabulation[id_egg][id_floor-j]) for j in 2:(id_floor-1)],
                    
                    #due to index starts at 1,the last worst case has to be separated
                    [1+tabulation[id_egg-1][id_floor-1]])) 
        end
    end
    return tabulation[num_of_eggs][num_of_floors]
end


# In[4]:


egg_drop(num_of_floors,num_of_eggs)


# In[ ]:




