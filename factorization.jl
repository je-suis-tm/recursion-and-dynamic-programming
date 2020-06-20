
# coding: utf-8

# In[1]:

#global list is the key
#otherwise we will lose the list throughout iterations
global factors=[]


# In[2]:


function factorization(num)
    
    #negative and float should be excluded
    if (num<0) || !(isinteger(num))
        
        error("negative or float is not allowed")
        
    end
   
    #if n is smaller than 4 
    #prime number it is
    if num>4
            
        #exclude 1 and itself
        #the largest factor of n can not exceed the half of n
        #because 2 is the smallest factor
        #the range of factors we are gonna try starts from 2 to fld(num,2)+1
        #int function to solve the odd number problem
        for i in 2:(fld(num,2)+1)
            
            #the factorization process
            if num%i==0
                
                push!(factors,i)

                #return is crucial
                #if the number is not a prime number
                #it will stop function from appending non-prime factors
                #the next few lines will be ignored
                return factorization(Int32(num/i))
                
            end

        end
            
    end
    
    #append the last factor    
    #it could be n itself if n is a prime number
    #in that case there is only one element in the list
    #or it could be the last indivisible factor of n which is also a prime number
    push!(factors,num)
    
    if length(factors)==1
        
        println(num," is a prime number")
        empty!(factors)
        
    end
        
end


# In[3]:


factorization(71392643)


# In[4]:


print(factors)

