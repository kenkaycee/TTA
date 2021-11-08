"""Write a program that allows you to enter 4 numbers and stores them in a file called “Numbers”
 Have a go at ‘w’ ‘r’  ‘a’"""

# write the file 
#%%
filename = "Numbers.txt" # name of the text file 
with open(filename, "w") as file_object: # write new file Numbers.txt or overwrite if file exists
    for x in range(4): 
        file_object.write(input("Enter a number: "))
        file_object.write("\n") # write number on new line
file_object.close()

#%%

##read a file       
with open("Numbers.txt", "r") as file_object:
    data = file_object.read()
file_object.close()

print(data)


#%%
## append a number to Numbers text file 
with open("Numbers.txt", "a") as file_object:
    file_object.write(input("Enter additional number: "))
    file_object.write("\n")
file_object.close()


#%%
## read the file again to check if new number was added 
with open("Numbers.txt", "r") as file_object:
    data = file_object.read()
file_object.close()

print(data)
      
