
# coding: utf-8

# In[33]:


#the first function is to calculte the elements in each row
def row(n):
    list=[]
    if n==1:
        #base case
        return [1]
    else:
        for i in range(1,len(row(n-1))):
            #rolling sum all the values with 2 windows from the previous row
            #but we cannot include two boudary numbers 1 in this list
            temp=row(n-1)[i]+row(n-1)[i-1]
            list.append((temp))
            #append 1 for both front and rear of the list
        list.insert(0,1)
        list.append(1)
        
        return list

#the second function is to concatenate all rows together and reshape them
def concat(n):
    l=[]
    #the first loop is to concatenate all rows
    for j in range(1,n+1):
        list=row(j)
        #this loop is to reshape the row
        #i insert '' between each element in the row
        for k in range(1,j+j-1):
            #if k is the odd number, i insert ''
            if k%2!=0:
                list.insert(k,'')
                #i also need to add '' to both sides of rows
                #n-j=((n+n-1)-(j+j-1))/2
                #we set the n th row plus n-1 space as the total elements in a list
                #we minus the reshaped row (j+j-1)
                #we get the space for both sides
                #finally we divide it by 2 and add to both sides of the row
                #we append the list into a new list
        l.append(['']*(n-j)+list+['']*(n-j))
    
    
        
    return l

def printit(n):
    #print out each list inside a list
    for i in concat(n):
        print(i)

printit(6)

