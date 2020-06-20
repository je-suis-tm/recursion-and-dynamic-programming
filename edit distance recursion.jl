
# coding: utf-8

# In[1]:


#explanation can be found in dynamic programming version
# https://github.com/je-suis-tm/recursion/blob/master/edit%20distance%20dynamic%20programming.jl
#the only problem with recursion is that it is so freaking slow
#recursion is so inefficient in any programming language
#although it looks much more elegant than dynamic programming


# In[2]:


function edit_distance(text1,text2)
    
    if isempty(text1) || isempty(text2)
        
        return max(length(text1),length(text2))
        
    end
    
    #we are comparing characters here
    #to get string, we should do end:end
    if text1[end]==text2[end]
        
        replacement=0
        
    else
        
        replacement=1
        
    end
    
    steps=min(edit_distance(text1[1:end-1],text2)+1,
        edit_distance(text1,text2[1:end-1])+1,
        edit_distance(text1[1:end-1],text2[1:end-1])+replacement)
    
    return steps
    
end


# In[3]:


println(edit_distance("arsehole","asshoe"))

