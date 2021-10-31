"""
Task 2: Then write a loop program that ask the
user for an integer number and check if it is <
10. If it is < 10 then it keeps adding 1 to the
value.
"""

number = int(input("Enter a number: "))
while number < 10:
    print(f"since {number} < 10, add 1 to it")
    number+=1 
    print(f"new number: {number}")
    if number >= 10:
        break

     