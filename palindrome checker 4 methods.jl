
# coding: utf-8

# In[1]:

#check if a string is a palindrome
#reversing a string is extremely easy
#at first i was thinking about using pop function
#however, for an empty string, pop function is still functional
#it would not stop itself
#it would show errors of popping from empty list
#so i have to use the classic way, slicing
#each time we slice the final letter
#to remove the unnecessary marks, we have to use regular expression
function palindrome_slicing(rawtext)
    
    #regex is very different in julia
    #we need to use match attribute to get string
    text=[i.match for i in eachmatch(r"[a-zA-Z0-9]",lowercase(rawtext))]
    
    #use non recursive slicing
    if text[length(text):-1:1]==text
        
        return true
        
    else
        
        return false
        
    end
    
end


# In[2]:


function palindrome_recursion(text)
    
    #this is the base case, when string is empty
    #we just return empty
    if isempty(text)
        
        return text
    
    else
        
        #such a pain without a python style list+list
        return cat([text[end]],
            palindrome_recursion(text[1:end-1]),
            dims=1)
        
    end
    
end 


# In[3]:


function recursion_check(rawtext)
    
    #this part is the regular expression to get only characters
    #and format all of em into lower cases
    text=[i.match for i in eachmatch(r"[a-zA-Z0-9]",lowercase(rawtext))]
    
    if palindrome_recursion(text)==text
        
        return true
        
    else
        
        return false
        
    end
    
end


# In[4]:

#or creating a new list
#using loop to append popped items from the old list
function palindrome_list(rawtext)
    
    text=[i.match for i in eachmatch(r"[a-zA-Z0-9]",lowercase(rawtext))]
    
    new=String[]
    
    for i in 1:length(text)
        
        #be careful with append
        #append will create char type instead of string type
        push!(new,text[end-i+1])
        
    end
    
    if new==text
        
        return true
        
    else
        
        return false
        
    end
    
end


# In[5]:

#alternatively, we can use deque
#we pop from both sides to see if they are equal
#if not return false
#note that the length of string could be an odd number
#we wanna make sure the pop should take action while length of deque is larger than 1
function palindrome_deque(rawtext)
    
    text=[i.match for i in eachmatch(r"[a-zA-Z0-9]",lowercase(rawtext))]
    
    while length(text)>=1
        
        if pop!(text)!=popfirst!(text)
            
            return false
            
        end
        
    end
    
    return true
    
end


# In[6]:


#0.257236 seconds (636.24 k allocations: 31.108 MiB, 2.37% gc time)
@time begin
    
    recursion_check("Evil is a deed as I live!")
    
end


# In[7]:


#0.058568 seconds (87.67 k allocations: 4.231 MiB)
@time begin
   
    palindrome_slicing("Evil is a deed as I live!")
    
end


# In[8]:


#0.084145 seconds (140.27 k allocations: 6.717 MiB, 8.51% gc time)
@time begin
   
    palindrome_list("Evil is a deed as I live!")
    
end


# In[9]:


#0.062403 seconds (74.95 k allocations: 3.500 MiB)
@time begin
   
    palindrome_deque("Evil is a deed as I live!")
    
end


# In[10]:


#in julia, the fastest is still the slicing approach

