
# coding: utf-8

# In[1]:


#fractal is one of the interesting topics in geometry
#it is usually described by a recursive function
#voila,here we are!
import matplotlib.pyplot as plt


# In[2]:


#compute euclidean distance
def euclidean_distance(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5


# In[3]:


#simple solution to get coefficients of the equation
def get_line_params(x1,y1,x2,y2):
    
    slope=(y1-y2)/(x1-x2)
    intercept=y1-slope*x1
    
    return slope,intercept


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


#recursively plot symmetric pythagorean tree at 45 degree
# https://larryriddle.agnesscott.org/ifs/pythagorean/pythTree.htm
def pythagorean_tree(ax,top_left,top_right,bottom_left,
                     bottom_right,current_angle,line_len,n):
    
    #plot square
    ax.add_patch(plt.Rectangle(xy=bottom_left,width=line_len,height=line_len,
                          angle=current_angle,))
    
    if n==0:
        return
    else:
                
        #find mid point
        #midpoint has to satisfy two conditions
        #it has to be on the same line as bottom_left and bottom_right 
        #assume this line follows y=kx+b
        #the midpoint is (x,kx+b)
        #bottom_left is (α,kα+b),bottom_right is (δ,kδ+b)
        #the euclidean distance between midpoint and bottom_left should be
        #half of the euclidean distance between bottom_left and bottom_right
        #(x-α)**2+(kx+b-kα-b)**2=((α-δ)**2+(kα+b-kδ-b)**2)/4
        #apart from x,everything else in the equation is constant
        #this forms a simple quadratic solution to get two roots
        #one root would be between bottom_left and bottom_right which yields midpoint
        #and the other would be farther away from bottom_right
        #this function solves the equation via (-B+(B**2-4*A*C)**0.5)/(2*A)
        #alternatively,you can use scipy.optimize.root
        #the caveat is it does not offer both roots
        #a wrong initial guess could take you to the wrong root
        bottom_mid=get_datapoint(bottom_left,bottom_right,line_len/2)
        top_mid=get_datapoint(top_left,top_right,line_len/2)
        
        #compute the top point of a triangle
        #the computation is similar to midpoint
        #the euclidean distance between triangle_top and top_mid should be
        #half of the distance between top_mid and bottom_mid
        triangle_top=get_datapoint(top_mid,bottom_mid,
                                   line_len/2,direction='outer')
    
        #get top left for right square
        #the computation is similar to midpoint
        #the euclidean distance between triangle_top and rightsq_topleft 
        #should be the same as the distance between triangle_top and top_left
        rightsq_topleft=get_datapoint(triangle_top,top_left,
                                      line_len/(2**0.5),direction='outer')
        
        #get midpoint of the diagonal between rightsq_topleft and top_right
        #the computation is similar to midpoint
        #the euclidean distance between rightsq_diag_mid and rightsq_topleft 
        #should be half of the distance between rightsq_topleft and top_right
        rightsq_diag_mid=get_datapoint(top_right,rightsq_topleft,line_len/2)
        rightsq_topright=get_datapoint(rightsq_diag_mid,triangle_top,
                                       line_len/2,direction='outer')
        
        #get top left and right for left square similar to right square
        leftsq_topleft=get_datapoint(triangle_top,rightsq_topright,
                                     line_len,direction='outer')
        leftsq_topright=get_datapoint(triangle_top,top_right,
                                      line_len/(2**0.5),direction='outer')
        
        #recursive do the same for left square
        pythagorean_tree(ax,leftsq_topleft,leftsq_topright,
                         top_left,triangle_top,current_angle+45,
                         line_len/(2**0.5),n-1)
        
        #recursive do the same for right square
        pythagorean_tree(ax,rightsq_topleft,rightsq_topright,
                         triangle_top,top_right,current_angle-45,
                         line_len/(2**0.5),n-1)


# In[7]:


#initialize
top_left=(0,0)
top_right=(1,0)
bottom_left=(0,-1)
bottom_right=(1,-1)
n=5
current_angle=0
line_len=euclidean_distance(top_left,top_right)


# In[8]:


#viz
ax=plt.figure(figsize=(10,8)).add_subplot(111)
pythagorean_tree(ax,top_left,top_right,bottom_left,
                     bottom_right,current_angle,line_len,n)

#limit figure dimension for better viz
plt.ylim(min([bottom_left[1],bottom_right[1]]),
        max([top_left[1],top_right[1]])+euclidean_distance(
            top_left,top_right)*(n-2)
         )
plt.xlim(min([bottom_left[0],top_left[0]])-euclidean_distance(
            top_left,top_right)*(n-1)/2,
        max([bottom_right[0],top_right[0]])+euclidean_distance(
            top_left,top_right)*(n-1)/2,
         )

plt.axis('off')
plt.show()

