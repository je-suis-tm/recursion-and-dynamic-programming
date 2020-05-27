
# coding: utf-8

# In[1]:


#this is a test on how recursion with memory reduces time complexity


# In[2]:


#this is the fibonacci recursion function without memory
#it is basically algorithm 101 for any coding language
function fib(n)
    
    if n==1
        return 1
    elseif n==2
        return 1
    elseif n<=0
        printstyled("Invalid input",color=:red)
        return
    else
        return fib(n-1)+fib(n-2)
    
    end
end


# In[3]:


#i need a global dictionary to do the memorization
#or i can change function mmz(n) into mmz(n,memoization)
global memoization=Dict(1=>1,2=>1)


# In[4]:


#mmz(n) is recursion with memory
#everytime we do the calculation, we store it in the dictionary
#i denote the key as the n th fibonacci number
#the value as the number itself
#if we can find the key in dictionary
#we simply return the value
#if not, we compute and update the dictionary then return the value
function mmz(n)
    
    if n<=0
        printstyled("Invalid input",color=:red)
        return
    end    
    
    if !(n in keys(memoization))
        global memoization[n]=mmz(n-1)+mmz(n-2)
    end
    
    return memoization[n]
end


# In[5]:


#using ijulia inline magic
#equivalent to %timeit in ipython
#0.000093 seconds
@time begin
    fib(20)
end


# In[6]:


#0.019746 seconds (5.60 k allocations: 335.035 KiB)
#it seems to be slower
#but if we compute mmz(30) now
#its much faster than fib(30)
@time begin
    mmz(20)
end


# In[7]:


#0.021588 seconds
@time begin
    fib(30)
end


# In[8]:


#0.000023 seconds (52 allocations: 832 bytes)
@time begin
    mmz(30)
end

