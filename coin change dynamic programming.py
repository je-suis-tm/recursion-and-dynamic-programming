
# coding: utf-8

# In[1]:


#coin change is a straight forward dynamic programming problem
#you are given one note and a set of coins of different values
#assuming you have infinite supply of coins of different values
#we need to compute different ways of making change
#the order of the coins doesnt matter in this case
#more details can be found in the following link
# https://www.geeksforgeeks.org/coin-change-dp-7/
#the script can also be done in recursion
# https://github.com/je-suis-tm/recursion-and-dynamic-programming/blob/master/coin%20change%20recursion.py


# In[2]:


#to solve this problem via tabulation
#we divide one big problem into two sub problems
#the case where coin of η value is excluded in the solutions
#and the case where at least one coin of η value is included
def coin_change(num,choice):
    
    #create matrix (num+1)*leng(choice)
    #the raison d'être is the computation starts from 0 to num
    #0 is when num is perfectly substituted by coins
    tabulation=[[0 for _ in range(len(choice))] for _ in range(num+1)]
    
    #initialize
    #when the remain value happens to be η
    #one solution is found
    for i in range(len(choice)):

        tabulation[0][i]=1
    
    #since we initialize the null case
    #the outerloop starts from 1
    for i in range(1,num+1):

        for j in range(len(choice)):
            
            if i-choice[j]>=0:

                #the case where at least one coin of η value is included
                #we just need the computation where η is deducted
                include=tabulation[i-choice[j]][j]
                        
            else:

                include=0

            #the case where coin of η value is excluded in the solutions
            if j>=1:

                exclude=tabulation[i][j-1]

            else:

                exclude=0
            
            #two sub problems merge into a big one
            tabulation[i][j]=exclude+include            

    #get the final answer
    return tabulation[num][len(choice)-1]


# In[3]:


coin_change(10,[1,2,3])

