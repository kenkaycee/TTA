"""
Write a program that asks a user for their favourite number between 1 and 100 and 
then tells them a joke based on the number. You should use a minimum of 3 jokes.
"""

#Solution
fav_number= int(input("Enter favourite number between 1 and 100: "))
if fav_number == 7:
  print("\nYour favourite number is", str(fav_number))  
  print("\nHow do you make seven even? Take away the S!")
  
elif fav_number == 6: 
  print("\nYour favourite number is", str(fav_number))    
  print("\nEverybody knows that 7 ate 9, but why?Because he needed to eat three squared meals a day!")
  
elif fav_number == 4:
  print("\nYour favourite number is", str(fav_number))    
  print("\nWhy couldn’t four get into the night club? Because he was two squared!")

elif fav_number < 1 or fav_number > 100:
  print("\nPlease enter a number between 1 and 100")

else:
  print("Your favourite number is", str(fav_number))  