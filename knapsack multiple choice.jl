
# coding: utf-8

# In[1]:


#this is a more advanced knapsack problem
#we have a new variable called groups
#we are only allowed to select at most one item from each group
#please note julia version is a lot more complex than python version
#simply becuz julia starts index at 1 and doesnt allow negative number indexing
#please check the following link for the basic knapsack problem
# https://github.com/je-suis-tm/recursion-and-dynamic-programming/blob/master/knapsack.jl


# In[2]:


#solve multiple choice knapsack via dynamic programming
function knapsack_multichoice(total_weight,values,weights,groups)
        
    #julia starts index at 1 which is why we use length(values)
    #create a nested list with size of number of items*weights
    array=[[0 for _ in 1:total_weight] for _ in 1:length(values)] 
    path=[[[] for _ in 1:total_weight] for _ in 1:length(values)]

    #now we begin our traversal on all elements in matrix
    for i in 1:length(values)
        for j in 1:total_weight 
            
            #-1 doesnt work as index in julia
            #have to find a way to get around
            if i==1 
                if weights[1]<=j
                    array[1][j]=values[1]
                    path[1][j]=[1]
                end
                continue
            end
 
            #this is the part to check if adding item i would exceed the current capacity j
            #if it does,we go to the previous status
            #if not,we shall find out whether adding item i would be the new optimal
            if weights[i]<j
                
                #initialize
                subset_max=0
                target=1                
                    
                #we only select one item from each group
                #we will find the item that maximizes the value in each group
                prev_group=groups[i]-1

                #get column of the matrix
                subset=[row[j-weights[i]] for row in array]

                #find the item that maximizes the value in the previous group
                for k in 1:length(values)
                    if groups[k]==prev_group && subset[k]>subset_max
                        subset_max=subset[k]
                        target=k
                    end
                end
                                        
                #dynamic programming
                if subset_max+values[i]>array[i-1][j]
                    array[i][j]=subset_max+values[i]
                    path[i][j]=[path[target][j-weights[i]];[i]]
                elseif subset_max+values[i]==array[i-1][j] && weights[i]<weights[path[i-1][j][end]]
                    array[i][j]=subset_max+values[i]
                    path[i][j]=[path[target][j-weights[i]];[i]]
                else
                    array[i][j]=array[i-1][j]
                    path[i][j]=path[i-1][j]
                end    
                
            elseif weights[i]==j
                
                #dynamic programming
                if values[i]>array[i-1][j]
                    array[i][j]=values[i]
                    path[i][j]=[i]                        
                elseif values[i]==array[i-1][j] && weights[i]<weights[path[i-1][j][end]]
                    array[i][j]=values[i]
                    path[i][j]=[i]                       
                else
                    array[i][j]=array[i-1][j]
                    path[i][j]=path[i-1][j]
                end    
                
            else                 
                array[i][j]=array[i-1][j]
                path[i][j]=path[i-1][j]
            end
        end
    end
    return array,path
end


# In[3]:


#a simple test
values=[60,80,100,110,120,150]
weights=[10,15,20,25,30,35]
groups=[0,0,1,1,2,2]
total_weight=50


# In[4]:


array,path=knapsack_multichoice(total_weight,values,
                                weights,groups)

println(array[length(weights)][total_weight])
println(path[length(weights)][total_weight])


