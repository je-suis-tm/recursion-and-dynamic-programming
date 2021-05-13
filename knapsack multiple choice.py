
# coding: utf-8

# In[1]:


#this is a more advanced knapsack problem
#we have a new variable called groups
#we are only allowed to select at most one item from each group
#please check the following link for the basic knapsack problem
# https://github.com/je-suis-tm/recursion-and-dynamic-programming/blob/master/knapsack.py


# In[2]:


#solve multiple choice knapsack via dynamic programming
def knapsack_multichoice(total_weight,values,weights,groups):
        
    #python starts index at 0 which is why we use len(values)+1
    #create a nested list with size of (number of items+1)*(weights+1)
    array=[[0 for _ in range(total_weight+1)] for _ in range(len(values)+1)] 
    path=[[[] for _ in range(total_weight+1)] for _ in range(len(values)+1)]

    #now we begin our traversal on all elements in matrix
    #note we would be using i-1 to imply item i
    for i in range(1,len(values)+1):
        for j in range(1,total_weight+1):                         
                
            #this is the part to check if adding item i would exceed the current capacity j
            #if it does,we go to the previous status
            #if not,we shall find out whether adding item i would be the new optimal
            if weights[i-1]<=j:
                
                #we only select one item from each group
                #we will find the item that maximizes the value in each group
                prev_group=groups[i-1]-1
                
                #initialize
                subset_max=0
                target=0                
                
                #get column of the matrix
                subset=[row[j-weights[i-1]] for row in array]
                
                #find the item that maximizes the value in the previous group
                for k in range(len(values)+1):
                    if groups[k-1]==prev_group and subset[k]>subset_max:
                        subset_max=subset[k]
                        target=k
                                        
                #dynamic programming
                if subset_max+values[i-1]>array[i-1][j]:
                    array[i][j]=subset_max+values[i-1]
                    path[i][j]=path[target][j-weights[i-1]]+[i-1]
                elif subset_max+values[i-1]==array[i-1][j] and                 weights[i-1]<weights[path[target][j-weights[i-1]][-1]]:
                    array[i][j]=subset_max+values[i-1]
                    path[i][j]=path[target][j-weights[i-1]]+[i-1]
                else:
                    array[i][j]=array[i-1][j]
                    path[i][j]=path[i-1][j]
            else:                 
                array[i][j]=array[i-1][j]
                path[i][j]=path[i-1][j]

    return array,path


# In[3]:


#a simple test
values=[60,80,100,110,120,150] 
weights=[10,15,20,25,30,35] 
groups=[0,0,1,1,2,2]
total_weight=50


# In[4]:


array,path=knapsack_multichoice(total_weight,values,weights,groups)

print(array[len(weights)][total_weight])
print(path[len(weights)][total_weight])

