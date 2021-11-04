"""
Create two arrays a and b, stack these two arrays vertically,  use the  np.dot and np.sum 
to calculate totals :
"""
# solution 
#%%
import numpy as np
# Create arrays a and b
a = np.arange(10, 19).reshape(3,3)
b = np.arange(19,28).reshape(3,3)


#%%
# Stack a and b vertically
v_stack = np.vstack((a,b))
print(v_stack)

#%% calculate totals using np.dot and np.sum
c= np.dot(a,b)
print(c)

print(np.sum(c))
