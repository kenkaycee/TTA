"""
Numpy Extension tasks
"""
"""task 1:
Create the following pattern without hardcoding. Use only NumPy  functions.
#array([1,1,1,2,2,2,3,3,3,1,2,3,1,2,3,1,2,3])

"""

#Solution to Task 1

import numpy as np
#%%
# Step 1: create array of sequence (1,1,1,2,2,2,3,3,3)
array_1 = np.arange(1,4)
x= np.repeat(array_1, 3) # repeat the sequence as above
print(x)

#%%
#Step 2: Create array of sequence (1,2,3,1,2,3,1,2,3)
array_2= np.array([1,2,3])
y= np.tile(array_2, 3) # repeat sequence as above 
print(y)

#%%
#step 3: concatenate x and y to get required array
final_array = np.concatenate((x,y))
print(final_array)

#%%
"""
Task 2:
    In two arrays a ( 1,2,3,4,5) and b ( 4,5,6,7,8,9) –remove all repeating  items 
    present in array b
"""
#%%
#Solution to task 2:

# create arrays a and b
a= np.array([1,2,3,4,5])
b= np.array([4,5,6,7,8,9])
unique_a=  np.setdiff1d(a,b) # gets values in a but not in b
print(unique_a)

## (Not part of the task but to get values in b not in a:)
unique_b = np.setdiff1d(b,a)
print(unique_b)

#%%
"""
Task 3:
    Get all items between 3 and 7 from a and b and sum them together
"""
#%%
# Solution to Task 3

#step 1: combine a and b
combine_array = np.concatenate((a,b))

#step 2: get items in combine_array between 3 and 7
bool_arr = np.array((combine_array >= 3) & (combine_array <= 7)) # set the boolean comparison
new_array = combine_array[bool_arr] # gets the items that satisfies the condition
print(new_array)
print(f"\nThe sum of the array is: {np.sum(new_array)}")
        
        