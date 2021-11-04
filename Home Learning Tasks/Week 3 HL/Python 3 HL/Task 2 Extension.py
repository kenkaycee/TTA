'''
Extension to task 2
• Ask the user for their target grade and print this with their mark
• If their target grade > exam grade display a suitable
message
• If their target grade = exam grade display a suitable
message
• If their target grade < exam grade display a suitable
message
'''

def mark_grade():
  target_grade = input("What's your target grade? ").upper()
  grade_list=["A", "B", "C", "D", "E", "F"]
  if target_grade not in grade_list or not target_grade.isalpha():
      print(f"Please choose grade from {grade_list}. Also, only enter alphabetical letters.")
      return mark_grade() 
   
  percent_mark = float(input("What's your percentage score? "))  

  if percent_mark >= 90 and percent_mark <= 100: 
    grade = "A"
    print(f"\nYou scored {grade} in Coding 101.")

  elif percent_mark >= 80 and percent_mark < 90:
    grade = "B"
    print(f"\nYou scored {grade} in Coding 101.")

  elif percent_mark >= 70 and percent_mark < 80:
    grade = "C"
    print(f"\nYou scored {grade} in Coding 101.")

  elif percent_mark >= 60 and percent_mark < 70:
    grade = "D"
    print(f"\nYou scored {grade} in Coding 101.")
  
  elif percent_mark >= 40 and percent_mark < 60:
    grade = "E"
    print(f"\nYou scored {grade} in Coding 101.")

  elif percent_mark >=0 and percent_mark < 40:
    grade = "F"
    print(f"\nYou scored {grade} in Coding 101.")
  else:
    print("Incorrect entry, percentage score must be between 0 and 100. Please enter your correct mark: \n")
    return mark_grade()

  
  if target_grade > grade:
    print(f"Your Target grade was: {target_grade}")
    print("Super congrats, you achieved more than your target. Keep up the hardwork!!")

  elif target_grade == grade:
    print(f"Your target grade was: {target_grade}")   
    print("Congrats, you achieved your target.")

  else:
    print(f"Your target grade was: {target_grade}")   
    print("You performed below your target. Don't give up; keep working hard.")     
    
mark_grade()

