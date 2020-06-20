
# coding: utf-8

# In[1]:


def pascal_triangle(n):
    
    row=[]
    
    #base case
    if n==1:
        return [1]
    else:
        
        #calculate the elements in each row
        for i in range(1,n-1):
            
            #rolling sum all the values within 2 windows from the previous row
            #but we cannot include two boundary numbers 1 in this row
            temp=pascal_triangle(n-1)[i]+pascal_triangle(n-1)[i-1]
            row.append((temp))
            
        #append 1 for both front and rear of the row
        row.insert(0,1)
        row.append(1)
        
        return row
    


# In[2]:


def printit(n):
    
    rows=[]
        
    #the first loop is to concatenate all rows
    for j in range(1,n+1):
        
        row=pascal_triangle(j)
        
        #this loop is to reshape the row
        #insert '' between each element in the row
        for k in range(1,j+j-1):
            
            #if index k is an odd number,insert ''
            if k%2!=0:
                row.insert(k,'')
                
        #need to add '' to both sides of rows
        #n-j=((n+n-1)-(j+j-1))/2
        #we set the n th row plus n-1 space as the total elements in a row
        #we minus the reshaped row (j+j-1)
        #we get the space for both sides
        #finally we divide it by 2 and add to both sides of the row
        #we append the styled row into rows
        rows.append(['']*(n-j)+row+['']*(n-j))    
    
    #print out each row
    for i in rows:
        print(i)


# In[3]:

#using memoization
global memoization
memoization={1:[1]}

def mmz(n):
    
    global memoization
    
    if n not in memoization:
        
        row=[]
        
        for i in range(1,n-1):
            
            #rolling sum all the values within 2 windows from the previous row
            #but we cannot include two boundary numbers 1 in this row
            temp=mmz(n-1)[i]+mmz(n-1)[i-1]
            row.append((temp))
            
        #append 1 for both front and rear of the row
        row.insert(0,1)
        row.append(1)
        
        memoization[n]=row
        
    return memoization[n]


# In[4]:


def printit_mmz(n):
    
    rows=[]
        
    #the first loop is to concatenate all rows
    for j in range(1,n+1):
        
        #need to be careful with copy
        #use list comprehension instead of deepcopy
        row=[i for i in mmz(j)]
        
        #this loop is to reshape the row
        #insert '' between each element in the row
        for k in range(1,j+j-1):
            
            #if index k is the odd number,insert ''
            if k%2!=0:
                row.insert(k,'')
                
        #need to add '' to both sides of rows
        #n-j=((n+n-1)-(j+j-1))/2
        #we set the n th row plus n-1 space as the total elements in a row
        #we minus the reshaped row (j+j-1)
        #we get the space for both sides
        #finally we divide it by 2 and add to both sides of the row
        #we append the styled row into rows
        rows.append(['']*(n-j)+row+['']*(n-j))    
    
    #print out each row
    for i in rows:
        print(i)
      


# In[5]:

#apparently memoization is faster

#7.04 ms ± 325 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
get_ipython().run_line_magic('timeit', 'printit(7)')


# In[6]:


#1.12 ms ± 10.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
get_ipython().run_line_magic('timeit', 'printit_mmz(7)')

