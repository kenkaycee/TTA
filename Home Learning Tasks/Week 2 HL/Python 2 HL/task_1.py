"""
Task 1: Write a program that asks the user for
an integer number and checks if it is > 10. If it
is, it will print “Number is Greater than 10”,
else “Number is smaller than 10”.
"""

#Solution
number= int(input("Enter a number: "))
if number > 10:
  print("Number is greater than 10.")
elif number == 10:
  print("Number is equals to 10")  
else:
  print("Number is smaller than 10.")