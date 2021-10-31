'''Task 1: 
Write a program that does the following:
a) Stores a random number (1-10) in a variable – see hint below.
b) Asks a user for their name and stores this in a variable.
c) Asks a user to guess the number between 1 and 10.
d) Tells the user whether they have guessed correctly'''

## Solution
import random # module used to create random numbers 

number= random.randint(1,10) # random numbers between 1 and 10
name= str(input("What's your name: ")) # ask user to enter therir name
print(f"\n{name.capitalize()}, guess a number between 1 and 10\n")
guess= int(input("What is your guess? ")) # ask user to guess a number 
if guess==number:
  print(f"\nMy number is {number}, you guessed {guess}. Congrats, you guessed correctly.")
else:
  print(f"\nMy number is {number}, you guessed {guess}. Sorry, your guess is wrong.")


