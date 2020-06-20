
# coding: utf-8

# In[1]:


function pascal_triangle(n)
    
    row=Any[]
    
    #base case
    if n==1
        
        return Any[1]
        
    elseif n==2
        
        return Any[1,1]
        
    else
        
        #calculate the elements in each row
        for i in 2:n-1
            
            #rolling sum all the values within 2 windows from the previous row
            #but we cannot include two boundary numbers 1 in this row
            push!(row,pascal_triangle(n-1)[i-1]+pascal_triangle(n-1)[i])
        
        end
        
        #append 1 for both front and rear of the row
        pushfirst!(row,1)
        push!(row,1)
    
    end
    
    return row
    
end


# In[2]:


function styled_row(nested)
    
    #the first loop is to concatenate all rows
    for i in 1:length(nested)
        
        temp=nested[i]
        
        #this loop is to reshape the row
        #insert '' between each element in the row
        for j in 2:(2*i-1)
            
            #if index k is an even number,insert ''
            if j%2==0
                
                insert!(temp,j,"")
                
            end
            
        end
        
        #need to add '' to both sides of rows
        #length(nested)-i=((length(nested)+length(nested)-1)-(i+i-1))/2
        #we set the n th row plus n-1 space as the total elements in a row
        #we minus the reshaped row (i+i-1)
        #we get the space for both sides
        #finally we divide it by 2 and add to both sides of the row
        #we append the styled row into rows
        nested[i]=cat(fill("",length(nested)-i),temp,fill("",length(nested)-i),dims=1)
        
    end
    
    return nested
    
end


# In[3]:

#print out each row
function printit(n)
    
    nested=Any[]
    
    for i in 1:n
        
        push!(nested,pascal_triangle(i))
        
    end
    
    for i in styled_row(nested)
        
        println(i)
        
    end
    
end


# In[4]:


#using memoization


# In[5]:


function mmz(n)
        
    row=Any[]
    
    if !(n in keys(memoization))
        
        #rolling sum all the values within 2 windows from the previous row
        #but we cannot include two boundary numbers 1 in this row
        for i in 2:n-1
        
            push!(row,mmz(n-1)[i-1]+mmz(n-1)[i])
        
        end
    
        #append 1 for both front and rear of the row
        pushfirst!(row,1)
        push!(row,1)
        
        global memoization[n]=row
        
    end
        
    return memoization[n]
    
end


# In[6]:


function printit_mmz(n)
    
    global memoization=Dict(1=>Any[1],2=>Any[1,1])
    
    nested=Any[]
    
    for i in 1:n
        
        push!(nested,mmz(i))
        
    end
    
    for i in styled_row(nested)
        
        println(i)
        
    end
    
end


# In[7]:


#0.021448 seconds (1.95 k allocations: 72.875 KiB)
@time begin
    
    printit(5)
    
end


# In[8]:


#0.355459 seconds (344.14 k allocations: 17.351 MiB)
@time begin
    
    printit_mmz(5)
    
end


# In[9]:


#3.822380 seconds (36.60 M allocations: 2.678 GiB, 8.57% gc time)
@time begin
    
    printit(10)
    
end


# In[10]:


#0.232830 seconds (7.27 k allocations: 254.938 KiB)
@time begin
    
    printit_mmz(10)
    
end

#at the first glance,memoization isnt faster
#as the number grows larger,memoization reveals its true nature