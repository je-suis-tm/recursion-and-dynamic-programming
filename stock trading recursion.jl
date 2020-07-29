# coding: utf-8


# In[1]: 


#a simple day trading game
#day trader is only allowed to make at maximum two trades
#the strategy is long only
#lets find out the maximum profit

#more details can be found in the following link
# https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/

#an alternative version in dynamic programming exists
#its done by using a different approach
#strongly recommend you to take a look
# https://github.com/je-suis-tm/recursion-and-dynamic-programming/blob/master/stock%20trading%20dynamic%20programming.jl


# In[2]:


#compute the maximum profit for long only strategy
function compute_profit(prices)
    
    #initialize maximum price with the close price
    max_price=prices[end]
    
    #initialize minimum price with the open price
    min_price=prices[1]
    
    #initialize indices
    left=1
    right=length(prices)
    minind=1
    maxind=length(prices)
    
    #we have two indices moving at the same time
    #one from left to find the minimum value
    #the other from right to find the maximum value
    #we are not looking for global minimum
    #we only want local minimum before the global maximum
    while left<maxind && right>minind
        
        #when a larger value is found
        #update accordingly
        if prices[right]>max_price

            max_price=prices[right]
            maxind=copy(right)

        end
    
        #the same applies to a smaller value
        if prices[left]<min_price

            min_price=prices[left]
            minind=copy(left)

        end    
        
        left+=1
        right-=1
        
    end
    
    #maximum profit
    profit=max_price-min_price
    
    #when we lose money
    #abort the trade
    if profit<0
        
        profit=0
        
    end
    
    return profit
    
end


# In[3]:


#there are two scenarios to maximize the profit
#one trade or two trades
#since we can execute two transactions
#we split the array at an iterating index i into half
#we find out the maximum profit we can obtain from both halves
function stock_trading(prices,ind)
    
    #prevent index error
    if ind+1==length(prices)
        
        return 0
        
    end
    
    #split
    upper=prices[1:ind]
    lower=prices[ind+1:end]
    
    #compute profit
    profit=compute_profit(lower)+compute_profit(upper)
    
    #compare recursively
    return max(profit,stock_trading(prices,ind+1))
    
end


# In[4]:


stock_trading([10,22,5,75,65,80],1)


# In[5]:


stock_trading([2,30,15,10,8,25,80],1)


# In[6]:


stock_trading([100,30,15,10,8,25,80],1)


# In[7]:


stock_trading([90,70,35,11,5],1)
