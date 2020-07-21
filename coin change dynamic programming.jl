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
# https://github.com/je-suis-tm/recursion-and-dynamic-programming/blob/master/coin%20change%20recursion.jl


# In[2]: 


#to solve this problem via tabulation
#we divide one big problem into two sub problems
#the case where coin of η value is excluded in the solutions
#and the case where at least one coin of η value is included
function coin_change(num,choice)
    
    #create matrix (num+1)*length(choice)
    #the raison d'être is the computation starts from 0 to num
    #0 is when num is perfectly substituted by coins
    tabulation=[[0 for _ in 1:length(choice)] for _ in 1:num+1]
    
    #initialize
    #when the remain value happens to be η
    #one solution is found
    for i in 1:length(choice)

        tabulation[1][i]=1

    end
    
    #since we initialize the null case
    #the outerloop starts from 2
    #i actually refers to i-1
    for i in 2:num+1

        for j in 1:length(choice)
            
            #annoying part of julia
            #if index starts at zero
            #will be a lot easier
            if i-choice[j]>=1

                #the case where at least one coin of η value is included
                #we just need the computation where η is deducted
                include=tabulation[i-choice[j]][j]
                        
            else

                include=0

            end
            
            #the case where coin of η value is excluded in the solutions
            if j>=2

                exclude=tabulation[i][j-1]

            else

                exclude=0

            end
            
            #two sub problems merge into a big one
            tabulation[i][j]=exclude+include            

        end

    end
    
    #get the final answer
    return tabulation[num+1][length(choice)]
    
end


# In[3]: 


coin_change(10,[1,2,5])
