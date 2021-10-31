
"""
Write a program which will ask for two numbers from a user. Then
offer a menu to the user giving them a choice of operator:
e.g. – Enter “a” if you want to add
“b” if you want to subtract
Include +, -, /, *, ** square (to the power of). Once the user has
selected which operator they wish to use, perform the calculation.
"""

#solution 


a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
choice_of_operation= input("What mathematical operation do you want to perform: ")
    
if choice_of_operation == "a":
    operation = a + b
    print("Perform addition:")
    print(f"{a} + {b} is: {operation}.")
    
elif choice_of_operation == "b":
    operation = a - b
    print("\nPerform subtraction")
    print(f"{a} minus {b} is: {operation}.")
        
elif choice_of_operation == "c":
    operation = a * b
    print("\nPerform multiplication")
    print(f"{a} times {b} is: {operation}. ")
        
elif choice_of_operation == "d":
    operation = a / b
    print("\nPerform division")
    print(f"{a} divided by {b} is: {operation}.")
        
elif choice_of_operation == "e":
    operation = a ** b
    print("\nExponetiate")
    print(f"{a} raised to the power of {b} is: {operation}.")
                
else: 
    operation= "Please choose from the following letters: (a,b,c,d,e) to perform operation!"
        
        
       
    