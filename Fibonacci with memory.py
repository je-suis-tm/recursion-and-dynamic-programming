
# coding: utf-8

# In[10]:


global mem
mem={1:1,2:1}
import datetime as dt

def fib(n):
    if n in mem:
        return mem[n]


    else:
        mem[n]=(fib(n-1)+fib(n-2))
        return mem[n]

def f(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
    
def compare(n):
    t1=dt.datetime.now()
    f(n)
    t2=dt.datetime.now()
    print('recursion: ',t2-t1)
    
    t1=dt.datetime.now()
    fib(n)
    t2=dt.datetime.now()
    print('recursion with memory: ',t2-t1)


# In[11]:


compare(20)


# In[7]:




