"""
Write a program which will ask for two numbers
from a user. Then offer an option menu to the user
giving them a choice of maths operators. Once the
user has selected which operator they wish to use,
perform the calculation by using a procedure and
passing parameters.
"""

def maths_operation(inp_num1, inp_num2):
  first_num= inp_num1
  second_num= inp_num2
  
  choice_of_operation= input("\nWhat mathematical operation do you want to perform: ")

  if choice_of_operation == "addition" or  choice_of_operation == "Addition":
    output = inp_num1 + inp_num2
    print(f"{inp_num1} plus {inp_num2} = {output}")
    

  elif choice_of_operation == "subtraction" or  choice_of_operation == "Subtraction":
    output = inp_num1 - inp_num2
    print(f"{inp_num1} minus {inp_num2} = {output}")
    
  
  elif choice_of_operation == "division" or  choice_of_operation == "Division":
    output = inp_num1 / inp_num2
    print(f"{inp_num1} divided by {inp_num2} = {output} ")
    

  elif choice_of_operation == "multiplication" or  choice_of_operation == "Multiplication":
    output = inp_num1 * inp_num2
    print(f"{inp_num1} multiplied by {inp_num2} = {output} ")
    

  elif choice_of_operation == "exponentiation" or  choice_of_operation == "Exponentiation":
    output = inp_num1 ** inp_num2
    print(f"{inp_num1} raised to the power of {inp_num2} = {output}")
    

first_num= int(input("Enter first number: "))
second_num=int(input("Enter second number: "))

maths_operation(first_num, second_num)
