
# coding: utf-8

# In[1]:


#its also called levenshtein distance
#it can be done via recursion too
#the recursion version is much more elegant yet less efficient
# https://github.com/je-suis-tm/recursion/blob/master/edit%20distance%20recursion.jl

#edit distance is to minimize the steps transforming one string to another
#the way to solve this problem is very similar is to knapsack
#assume we have two strings text1 and text2
#we build a matrix with the size of (length(text1)+1)*(length(text2)+1)

#there are three different ways to transform a string
#insert,delete and replace
#we can use any of them or combined
#lets take a look at the best case first
#assume string text1 is string text2
#we dont need to do anything
#so 0 steps would be the answer
#for the worst case
#when string text1 has nothing in common with string text2
#we would have to replace the whole string text1
#the steps become the maximum step which is max(length(text1),length(text2))
#for general case,the number of steps would fall between the worst and the best case
#assume we are at i th letter of string text1 and j th letter string text2
#if we wanna get the optimal steps of transforming string text1 to string text2
#we have to make sure at each letter transformation
#text1[1:i] and text2[1:j] have reached their optimal status
#otherwise,we could always find another combination of insert,delete and replace
#to get a "real" optimal text1[1:i] and text2[1:j]
#it would make our string transformation not so optimal any more
#it is the same logic as the optimization of knapsack problem
#after we set our logic straight
#we would take a look at three different approaches
#lets take a look at insertion
#basically we need to insert j th letter from string text2 into string text1 at i th position
#the cumulated steps we have taken should be matrix[i][j-1]+1
#matrix[i][j-1] is the steps for text1[1:i] to text2[1:j]
#for delete,it is vice versa
#the cumulated steps we have taken should be matrix[i-1][j]+1
#for replacement,it is a lil bit tricky
#there are two scenarios
#if text1[i-1]==text2[j-1]
#it should be matrix[i-1][j-1]
#we dont need any replacement at all
#else,it should be matrix[i-1][j-1]+1
#we replace i th letter of string text1 with j th letter of string text2
#after we managed to understand three different approaches
#we want to take the minimum number of steps among these three approaches
#throughout the iteration of different positions of both strings
#in the end,we would get the optimal steps to transform one string to another,YAY


# In[2]:


function edit_distance(text1,text2)
    
    len1=length(text1)+1
    len2=length(text2)+1
    
    #this part is to create a matrix of (length(text1)+1)*(length(text2)+1)
    matrix=[[0 for _ in 1:len2] for _ in 1:len1]
    
    for i in 1:len1
        
        matrix[i][1]=i-1
    
    end
    
    for i in 1:len2
        
        matrix[1][i]=i-1
        
    end
    
    #we take iterations on both string text1 and text2
    #next,we check if text1[i-1]==text2[j-1]
    #if yes,no replacement needed
    #if no,replacement needed
    #we take a minimum function to see which combination would give the minimum steps
    #eventually we got what we are after
    for i in 2:len1
        
        for j in 2:len2
            
            if text1[i-1]==text2[j-1]
                
                matrix[i][j]=min(matrix[i-1][j]+1,
                matrix[i][j-1]+1,
                matrix[i-1][j-1])
                
            else
                
                matrix[i][j]=min(matrix[i-1][j]+1,
                matrix[i][j-1]+1,
                matrix[i-1][j-1]+1)
                
            end
            
        end
        
    end
    
    return matrix[len1][len2]
    
end


# In[3]:


println(edit_distance("baiseé","bas"))

