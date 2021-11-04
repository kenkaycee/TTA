"""
Extract all odd numbers from array of 1-10
"""

import numpy as np
# create array of 1-10
#%%
array= np.arange(1,11)
print(array)

#%%
# print odd numbers in array
for i in array:
    if i % 2 != 0:
        print(f"{i} is an odd number.")