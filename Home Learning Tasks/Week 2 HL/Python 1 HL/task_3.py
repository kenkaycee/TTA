"""
Write a program that allows user to enter their favourite starter, main course, dessert and drink.
Concatenate these and output a message which says –“Your favourite meal is  .........with
 a glass of....”
"""
#Solution 
starter= input("Enter your favourite starter: ")
main_course = input("Enter main course: ")
dessert= input("Enter your favourite deseert: ")
drink= input("Enter your favourite drink: ")
print(f"\nYour favourite meal is {starter}, {main_course},and {dessert} with a glass of {drink}.")