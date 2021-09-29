
# coding: utf-8

# In[1]:


#another fractal script via recursion
#this script heavily involves analytic geometry
#a good material to help you rewind high school geometry
# https://youthconway.com/handouts/analyticgeo.pdf
import matplotlib.pyplot as plt


# In[2]:


#simple solution to get coefficients of the equation
def get_line_params(x1,y1,x2,y2):
    
    slope=(y1-y2)/(x1-x2)
    intercept=y1-slope*x1
    
    return slope,intercept


# In[3]:


#compute euclidean distance
def euclidean_distance(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5


# In[4]:


#standard solution to quadratic equation
def solve_quadratic_equation(A,B,C):
    x1=(-B+(B**2-4*A*C)**0.5)/(2*A)
    x2=(-B-(B**2-4*A*C)**0.5)/(2*A)
    return [x1,x2]


# In[5]:


#analytic geometry to compute target datapoints
def get_datapoint(pivot,measure,length,direction='inner'):
    
    #for undefined slope
    if pivot[0]==measure[0]:
        y1=pivot[1]+length
        y2=pivot[1]-length
        x1=pivot[0]
        x2=pivot[0]
    
    #for general cases
    else:

        #get line equation
        slope,intercept=get_line_params(pivot[0],pivot[1],
                                   measure[0],measure[1],)

        #solve quadratic equation
        A=1
        B=-2*pivot[0]
        C=pivot[0]**2-length**2/(slope**2+1)
        x1,x2=solve_quadratic_equation(A,B,C)

        #get y from line equation
        y1=slope*x1+intercept
        y2=slope*x2+intercept

    if direction=='inner':
        
        #take the one between pivot and measure points
        datapoint=min([(x1,y1),(x2,y2)],
                        key=lambda x:euclidean_distance(x,measure))
    else:
        
        #take the one farther away from measure points
        datapoint=max([(x1,y1),(x2,y2)],
                        key=lambda x:euclidean_distance(x,measure))
        
    return datapoint


# In[6]:


#recursively compute the coordinates of koch curve data points
#to effectively connect the data points,the best choice is to use turtle
#it would be too difficult to connect the dots via analytic geometry
def koch_snowflake(base1,base2,base3,n):

    #base case
    if n==0:        
        return
    
    else:
        
        #find mid point
        #midpoint between base1 and base2 has to satisfy two conditions
        #it has to be on the same line as base1 and base2
        #assume this line follows y=kx+b
        #the midpoint is (x,kx+b)
        #base1 is (α,kα+b),base2 is (δ,kδ+b)
        #the euclidean distance between midpoint and base1 should be
        #half of the euclidean distance between base1 and base2
        #(x-α)**2+(kx+b-kα-b)**2=((α-δ)**2+(kα+b-kδ-b)**2)/4
        #apart from x,everything else in the equation is constant
        #this forms a simple quadratic solution to get two roots
        #one root would be between base1 and base2 which yields midpoint
        #and the other would be farther away from base2
        #this function solves the equation via (-B+(B**2-4*A*C)**0.5)/(2*A)
        #alternatively,you can use scipy.optimize.root
        #the caveat is it does not offer both roots
        #a wrong initial guess could take you to the wrong root
        midpoint=get_datapoint(base1,base2,euclidean_distance(base1,base2)/2)

        #compute the top point of a triangle
        #the computation is similar to midpoint
        #the euclidean distance between triangle_top and midpoint should be
        #one third of the distance between base3 and midpoint
        triangle_top=get_datapoint(midpoint,base3,
                                   euclidean_distance(midpoint,base3)/3,
                                   direction='outer')

        #two segment points divide a line into three equal parts
        #the computation is almost the same as midpoint
        #the euclidean distance between segment1 and base1
        #should be one third of the euclidean distance between base2 and base1
        segment1=get_datapoint(base1,base2,euclidean_distance(base1,base2)/3)
        segment2=get_datapoint(base2,base1,euclidean_distance(base1,base2)/3)

        #compute the nearest segment point of the neighboring line
        segment_side_1=get_datapoint(base1,base3,euclidean_distance(base1,base3)/3)
        segment_side_2=get_datapoint(base2,base3,euclidean_distance(base2,base3)/3)

        #recursion
        yield [segment1,segment2,triangle_top]
        yield from koch_snowflake(base1,segment1,segment_side_1,n-1)
        yield from koch_snowflake(segment1,triangle_top,segment2,n-1)
        yield from koch_snowflake(triangle_top,segment2,segment1,n-1)
        yield from koch_snowflake(segment2,base2,segment_side_2,n-1)


# In[7]:


#set data points
point1=(0,0)
point2=(3,0)
point3=(3/2,3/2*(3**0.5))

#due to python floating point arithmetic
#a lot of data points could go wrong during the calculation
#unfortunately there is no panacea to this malaise
#unless we plan to use decimal package all the time
#when the depth of snowflake reaches 1
#one of the data points reach -1.1102230246251565e-16 on x axis
#when the depth of snowflake reaches 6
#we end up with complex root and things go wrong
n=4


# In[8]:


#collect coordinates
arr=list(koch_snowflake(point1,point2,point3,n))+list(
    koch_snowflake(point1,point3,point2,n))+list(
    koch_snowflake(point2,point3,point1,n))+[(point1,point2,point3)]
coordinates=[j for i in arr for j in i]


# In[9]:


#viz
#visually u can tell some of the data points are miscalculated
#purely caused by floating point arithmetic
ax=plt.figure(figsize=(5,5))
plt.scatter([i[0] for i in coordinates],
            [i[1] for i in coordinates],s=0.5)
plt.axis('off')
plt.show()
