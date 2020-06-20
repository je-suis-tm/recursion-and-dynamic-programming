#this has nothing to do with recursion algorithm
#it happened to be in the recursion chapter in my book
#so i kept it under recursion
#its about dynamic programming
#its kinda tricky to understand
#if you are familiar with convex optimization or lagrangian
#its better to use em instead of this


#knapsack problem is to maximize the value
#while having a weight constraint
#each value has a different weight
#the knapsack has a maximum capacity which is the constraint


#to solve the problem,we have to use recursive thinking
#lets create a list from 1 to the maximum capacity
#for each capacity in the list 
#we try to reach the optimal allocation of weight at the given capacity
#say we have c as the maximum capacity
#we remove the last item i
#we get weight c-w[i]
#we wanna make sure our allocation at c-w[i] is still the optimal
#by optimal,we mean for the same weight we can achieve the highest value
#if c-w[i] is not the optimal
#we can find another combo with the same weight but higher value
#we add the item i back into the knapsack then
#the new total value we get would be larger than the previous so-called optimal
#it will contradict the definition of optimal
#hence,for each capacity,we keep removing items
#until we reach base case 0,and it always stays the optimal at the given capacity


#to get the optimal status
#we shall do a traversal on all items
#we create a matrix called l with (number of items) * (maximum capacity)
#for each capacity level,we try to add a new item
#if adding new item causes the overall weight larger than the current capacity level
#the knapsack reverts to the previous status without item i which is l[i-1][j]
#if adding new item doesnt cause the overall weight bigger than the current capacity level
#we try to see whether adding item i would be the new optimal case
#so we compare the previous status with the status after adding item i
#the status after adding item i shall be l[i-1][j-w[i-1]]+v[i-1]
#we use j-w[i-1] cuz adding item i would reduce the capacity we have
#we have to use the current constraint level j to minus item i weight
#note that we use w[i-1] and v[i-1] instead of w[i] and v[i] to represent item i
#that is becuz weight and value list index at 0
#the alternative way is to insert 0 at index 0 for both v and w
#we would be able to use v[i] instead of v[i-1]


def knapsack(v,w,c):
    
    #as mentioned before
    #v indexes from 0 which is why we use len(v)+1
    #the same applies to c
    #in this section,we create a nested list with size of (number of items+1)*(c+1)
    l=[[0]*(c+1) for _ in range(len(v)+1)]

    #now we begin our traversal on all elements in matrix
    #i starts from 1 cuz we would be using i-1 to imply item i
    for i in range(1,len(v)+1):
        for j in range(c+1):
            
            #this is the part to check if adding item i would exceed the current capacity j
            #if it does,we go to the previous status
            #if not,we shall find out whether adding item i would be the new optimal
            if w[i-1]>j:
                
                l[i][j]=l[i-1][j]

            else:
                
                #we use max funcion to see if adding item i would be the new optimal
                l[i][j]=max(l[i-1][j],l[i-1][j-w[i-1]]+v[i-1])

    return l[len(v)][c]

print(knapsack([0,40,60,50,120],[0,10,15,20,30],50))
