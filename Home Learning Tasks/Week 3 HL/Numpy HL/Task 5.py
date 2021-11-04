"""
Convert a 1D array to a 2D array with 2 rows

"""
#%%
# solution 
import numpy as np
# Create 1d array
array_1d = np.array([1,2,3,4,5,6,7,8,9,10])

#%%
# convert the array to 2D array with two rows
array_2d = array_1d.reshape(2,5)

print(f"1D array: {array_1d} \n2D array with 2 rows: \n{array_2d}")
