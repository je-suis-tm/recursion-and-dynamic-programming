
# coding: utf-8

# In[1]:


#hanoi tower is the classic recursion
#the logic behind it is amazing
#rules can be seen from this website:
# https://en.wikipedia.org/wiki/Tower_of_Hanoi


# In[2]:


function hanoi(n,column1,column2,column3)
    
    #rule states that each time we can only move one element
    #so when the recursion reaches to base case 1
    #we print the movement of elements from column 1 to column 3
    if n==1
        println(column1," -> ",column3)
        return
    end
    
    #for the general case
    #the first step is to move everything above the base case from column 1 to column 2
    #note that we set print 1 to 3 when n reaches one
    #so in this case we reorder the function, replace column 3 with column 2
    #where elements actually move towards
    #the reorder is purely for printing
    hanoi(n-1,column1,column3,column2)
    
    #the second step is to move the base case from column 1 to column 3
    #we are only moving base case, thats why n=1
    hanoi(1,column1,column2,column3)
    
    #final step would be move everything above base case from column 2 to column 3
    hanoi(n-1,column2,column1,column3)
    
end


# In[3]:


#the best explanation should be
# https://www.python-course.eu/towers_of_hanoi.php


# In[4]:


hanoi(4,"Column A","Column B","Column C")

