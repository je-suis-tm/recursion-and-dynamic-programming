
# coding: utf-8

# In[1]:


#egg drop is a simple dynamic programming problem
#the player is given some number of eggs 
#to test eggs break by free fall from which floor
#more details can be found in the link below
# https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/


# In[2]:


#initialize
num_of_floors=40
num_of_eggs=5


# In[3]:


#to solve this problem via dp
#we test all the floor with the eggs
def egg_drop(num_of_floors,num_of_eggs):

    #create tabulation matrix
    tabulation=[[None for _ in range(num_of_floors+1)] for _ in range(num_of_eggs+1)]

    #when u got zero egg u got zero attempt
    tabulation[0]=[0]*(num_of_floors+1)

    #when u got one egg the number of attempts will always be the number of floors
    tabulation[1]=[ii for ii in range(num_of_floors+1)]

    #ground floor doesnt break eggs as its on the ground
    #first floor only takes one attempt no matter how many eggs we have
    for i in range(2,num_of_eggs+1):    
        tabulation[i][0]=0
        tabulation[i][1]=1

    #since we initialize the ground floor and the first floor
    #the loop starts from 2
    for id_egg in range(2,num_of_eggs+1):
        for id_floor in range(2,num_of_floors+1):

            #at the current position (id_egg,id_floor)
            #there are id_egg number of eggs and id_floor number of floors
            #we start to experiment the worst case via brute force
            #we drop eggs on each floor
            #there are id_floor*2 scenarios        
            #each floor can be the one that breaks the egg or doesnt break the eggs
            #hence we compute how many trials are required for each scenario
            #take the maximum first to obtain worst case for each floor
            #and take the minimum to obtain the minimum number of trials
            tabulation[id_egg][id_floor]=min(
                [1+max(
                    tabulation[id_egg-1][j-1],
                    tabulation[id_egg][id_floor-j]) for j in range(
                    1,id_floor+1)])

    return tabulation[num_of_eggs][num_of_floors]


# In[4]:


egg_drop(num_of_floors,num_of_eggs)

