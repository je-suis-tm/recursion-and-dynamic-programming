# coding: utf-8


# In[1]: 


#a simple day trading game
#day trader is only allowed to make at maximum two trades
#the strategy is long only
#lets find out the maximum profit

#more details can be found in the following link
# https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/

#an alternative version in recursion exists
#its done by using a different approach
#strongly recommend you to take a look
# https://github.com/je-suis-tm/recursion-and-dynamic-programming/blob/master/stock%20trading%20recursion.jl


# In[2]:


#there are two scenarios to maximize the profit
#one trade or two trades
#first we run a reverse iteration
#to obtain the maximum profit from one trade
#then we run a normal iteration
#to obtain the maximum profit
#from one trade plus the result from reverse iteration
function stock_trading(prices)
    
    #initialize the profit at zero
    profit=[0 for _ in 1:length(prices)]
    
    #initialize maximum price with the close price
    max_price=prices[end]
    
    #reverse order iteration
    for i in length(prices)-1:-1:1
        
        #update the maximum price to compute the maximum profit
        if prices[i]>max_price
            
            max_price=prices[i]
            
        end
        
        #two scenarios to get the maximum profit
        #either the previous iteration is larger
        #or this round of iteration
        profit[i]=max(profit[i+1],max_price-prices[i])
        
    end
    
    #initialize minimum price with the open price
    min_price=prices[1]
    
    #second round of iteration
    for i in 2:length(prices)
        
        #update the minimum price to compute the maximum profit
        if prices[i]<min_price
            
            min_price=prices[i]
            
        end
        
        #two scenarios to get the maximum profit
        #either the previous iteration is larger
        #or this round of iteration plus the result from single transaction
        profit[i]=max(profit[i-1],profit[i]+prices[i]-min_price)   
                
    end
    
    return profit[end]
    
end


# In[3]:


stock_trading([10,22,5,75,65,80])


# In[4]:


stock_trading([2,30,15,10,8,25,80])


# In[5]:


stock_trading([100,30,15,10,8,25,80])


# In[6]:


stock_trading([90,70,35,11,5])
