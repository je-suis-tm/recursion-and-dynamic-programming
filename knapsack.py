#this has nothing to do with recursion algorithm
#it happened to be in the recursion chapter in my book
#so i kept it under recursion
#its about dynamic programming
#its kinda tricky to understand


#knapsack problem is to maxmize the value
#while having a weight constraint
#each value has a different weight
#the knapsack has a maximum capacity which is the constraint


#to solve the problem, we have to use recursive thinking
#lets create a list of capacity
#before reaching the maximum capacity
#for each capacity in the list 
#we try to reach its own optimization
#say we have c as constrait
#we remove the last item i
#we get weight c-w[i]
#we wanna make sure c-w[i] is still optmized
#by optimized, we mean for the same weight we can achieve the highest value
#if n-w[i] is not optmized
#we can find another combo with the same weight but higher value
#we add back the item i into the knapsack then
#the total value we get would be larger than the previous so-called optmization
#it will contradict the definition of optimization
#hence, for each capacity,we keep removing items
#until we reach base case 0, and it always stays optimized


#to get final optmization on the constraint
#we shall do a traversal on all items
#we create a matrix called l with (number of items) * (maximum capacity)
#for each capacity level, we try to add a new item
#if the item weight is larger than the current capacity level
#the knapsack stays the previous status without item i which is l[i-1][j]
#if the item weight is smaller than the current capacity level
#we try to see whether adding item i would be the optimization
#so we compare the previous status with the status after adding item i
#the status after adding item i shall be l[i-1][j-w[i-1]]+v[i-1]
#we use j-w[i-1] cuz adding item i would reduce the capacity we have
#we have to use the current constraint level j to minus item i weight
#note that we use w[i-1] and v[i-1] instead of w[i] and v[i] to represent item i
#that is becuz weight and value list index at 0
#when we refer to the first item i, we intend to say item 1
#but computers refer to item 0
#so i-1 actually refers to the current item i
#the alternative way is to insert 0 at index 0 for both v and w
#we would be able to use v[i] instead of v[i-1]


def f(v,w,c):
  l=[]
  #as mentioned before
  #v indexes from 0 which is why we use len(v)+1
  #so that we get the real item i in our concept instead of item i-1 in computers concept
  #the same applies to c
  #in this section, we create a list consists of lists, which is a matrix
  #its actually a matrix of (number of items+1 )* (c+1)
  for i in range(len(v)+1):
    l.append([0]*(c+1))
  
    
  #now we begin our traversal on all elements in matrix
  #i starts from 1 cuz we would be using i-1 to imply item i in our concept
  #so we dont go outta index for the case of item 0
  #cuz there is no item -1
  for i in range(1,len(v)+1):
    for j in range(c+1):
        #this is the part to check if adding item i would exceed the current constraint level j
        #if it does, we go to the previous status
        #if not, we shall find out whether adding item i would be optimized
      if w[i-1]>j:
        l[i][j]=l[i-1][j]
      else:
          #we use max funcion to see if adding item i would be optimized
        l[i][j]=max(l[i-1][j],l[i-1][j-w[i-1]]+v[i-1])
  return l

print(f([0,60,100,120],[0,10,20,30],50))