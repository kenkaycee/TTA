"""
Replace all odd numbers in an array of 1-10 with the value -1
"""

#Solution 
#%%
import numpy as np
#create array of 1-10
array = np.arange(1,11)
print(array)

#%%

# create new array from array above replacing odd vlaues in array with -1
new_array = np.where(array % 2 != 0, -1, array)
print(new_array)



