
# coding: utf-8

# In[1]:


#fractal is one of the interesting topics in geometry
#it is usually described by a recursive function
#voila,here we are!
using Plots


# In[2]:


#define starting and ending points
#and the order of hilbert curve
n=4
starting_point=(0,0)
ending_point=(2^n-1,0)


# In[3]:


#the code for hilbert curve may look intimidating at the first glance
#it is extremely simple and straight forward
#julia version is slightly different
#as we cannot use yield like python
#coroutine in julia is too complicated
#maybe another day...
function hilbert_curve(coordinates,point1,point2,n)

    #unpack
    x_start,y_start=point1
    x_end,y_end=point2    

    #the function consists four different parts
    #which are 4 different rotations plus flips of a second order hilbert curve
    #0 degree second order hilbert curve
    if x_start<x_end && y_start==y_end
        
        #compute the grid length
        L=x_end-x_start
        
        #keypoints are starting and ending points
        #of 4 different first order hilbert curves
        #on a second order hilbert curve
        keypoints=[(x_start,y_start),(x_start,y_start-(L-1)/2),
        (x_start,y_start-(L-1)/2-1),(x_start+(L-1)/2,y_start-(L-1)/2-1),
        (x_start+(L-1)/2+1,y_start-(L-1)/2-1),(x_start+L,y_start-(L-1)/2-1),
        (x_start+L,y_start-(L-1)/2),(x_start+L,y_start)]
        
        #base case
        if n==1
            append!(coordinates,keypoints)
        else
            
            #recursion
            for i in 1:2:8
                hilbert_curve(coordinates,
                    keypoints[i],keypoints[i+1],n-1)
            end
        end
    end

    #180 degree second order hilbert curve
    if x_start>x_end && y_start==y_end
        L=x_start-x_end
        keypoints=[(x_start,y_start),(x_start,y_start+(L-1)/2),
        (x_start,y_start+(L-1)/2+1),(x_start-(L-1)/2,y_start+(L-1)/2+1),
        (x_start-(L-1)/2-1,y_start+(L-1)/2+1),(x_start-L,y_start+(L-1)/2+1),
        (x_start-L,y_start+(L-1)/2),(x_start-L,y_start)]
        if n==1
            append!(coordinates,keypoints)
        else
            for i in 1:2:8
                hilbert_curve(coordinates,
                    keypoints[i],keypoints[i+1],n-1)
            end
        end
    end
    
    #clockwise 90 degree horizontal flipped second order hilbert curve
    if x_start==x_end && y_start>y_end
        L=y_start-y_end
        keypoints=[(x_start,y_start),(x_start+(L-1)/2,y_start),
        (x_start+(L-1)/2+1,y_start),(x_start+(L-1)/2+1,y_start-(L-1)/2),
        (x_start+(L-1)/2+1,y_start-(L-1)/2-1),(x_start+(L-1)/2+1,y_start-L),
        (x_start+(L-1)/2,y_start-L),(x_start,y_start-L)]
        if n==1
            append!(coordinates,keypoints)
        else
            for i in 1:2:8
                hilbert_curve(coordinates,
                    keypoints[i],keypoints[i+1],n-1)
            end
        end
    end
    
    #clockwise 270 degree horizontal flipped second order hilbert curve
    if x_start==x_end && y_start<y_end
        L=y_end-y_start
        keypoints=[(x_start,y_start),(x_start-(L-1)/2,y_start),
        (x_start-(L-1)/2-1,y_start),(x_start-(L-1)/2-1,y_start+(L-1)/2),
        (x_start-(L-1)/2-1,y_start+(L-1)/2+1),(x_start-(L-1)/2-1,y_start+L),
        (x_start-(L-1)/2,y_start+L),(x_start,y_start+L)]
        if n==1
            append!(coordinates,keypoints)
        else
            for i in 1:2:8
                hilbert_curve(coordinates,
                    keypoints[i],keypoints[i+1],n-1)
            end
        end
    end
    coordinates
end


# In[4]:


#get coordinates
coordinates=hilbert_curve([],
    starting_point,ending_point,n);


# In[5]:


#viz
gr(size=(250,250))
fig=plot(legend=false,grid=false,axis=false,ticks=false)
plot!([i[1] for i in coordinates],
        [i[2] for i in coordinates])
fig



