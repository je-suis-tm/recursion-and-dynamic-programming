
# coding: utf-8

# In[1]:


#this has nothing to do with recursion algorithm
#it happened to be in the recursion chapter in my book
#so i kept it under recursion
#its about dynamic programming
#its kinda tricky to understand
#if you are familiar with convex optimization or lagrangian
#its better to use em instead of this


#knapsack problem is to maximize the value
#while having a weight constraint
#each value has a different weight
#the knapsack has a maximum capacity which is the constraint


#to solve the problem,we have to use recursive thinking
#lets create a list from 1 to the maximum capacity
#for each capacity in the list 
#we try to reach the optimal allocation of weight at the given capacity
#say we have c as the maximum capacity
#we remove the last item i
#we get weight capacity-weight[i]
#we wanna make sure our allocation at capacity-weight[i] is still the optimal
#by optimal,we mean for the same weight we can achieve the highest value
#if capacity-weight[i] is not the optimal
#we can find another combo with the same weight but higher value
#we add the item i back into the knapsack then
#the new total value we get would be larger than the previous so-called optimal
#it will contradict the definition of optimal
#hence,for each capacity,we keep removing items
#until we reach base case 0,and it always stays the optimal at the given capacity


#to get the optimal status
#we shall do a traversal on all items
#we create a matrix with (number of items) * (maximum capacity)
#for each capacity level,we try to add a new item
#if adding new item causes the overall weight larger than the current capacity level
#the knapsack reverts to the previous status without item i which is matrix[i-1][j]
#if adding new item doesnt cause the overall weight bigger than the current capacity level
#we try to see whether adding item i would be the new optimal case
#so we compare the previous status with the status after adding item i
#the status after adding item i shall be matrix[i-1][j-weight[i-1]]+value[i-1]
#we use j-weight[i-1] cuz adding item i would reduce the capacity we have
#we have to use the current constraint level j to minus item i weight


# In[2]:


function knapsack(value,weight,capacity)

    #in this section,we create a nested list with size of (number of items+1)*(capacity+1)
    matrix=[[0 for _ in 1:(capacity+1)] for _ in 1:(length(value)+1)]
    
    #now we begin our traversal on all elements in matrix
    #i starts from 2 cuz we would be using i-1 to imply item i
    for i in 2:(length(value)+1)
        
        for j in 2:(capacity+1)
            
            #this is the part to check if adding item i-1 would exceed the current capacity j
            #if it does,we go back to the previous status
            #if not,we shall find out whether adding item i-1 would be the new optimal
            if weight[i-1]>j
                
                matrix[i][j]=matrix[i-1][j]
                
            else
                
                #julia index starts from 1
                #which is a pain in the ass
                #when current capacity==the new item s weight
                #it creates an issue
                if j==weight[i-1]
                    
                    ind=1
                    
                else
                    
                    ind=j-weight[i-1]
                    
                end
                
                #we use max funcion to see if adding item i-1 would be the new optimal
                matrix[i][j]=max(matrix[i-1][j],
                matrix[i-1][ind]+value[i-1])
                
            end
            
        end
        
    end
    
    return matrix[length(value)+1][capacity+1]
    
end


# In[3]:


println(knapsack([0,50,60,60,120],[0,10,15,20,40],50))

