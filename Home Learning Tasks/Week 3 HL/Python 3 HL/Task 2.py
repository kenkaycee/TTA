"""
Write a program to ask a student for their percentage mark and convert this to a grade. The conversion will be
done in a function called mark_grade
"""

# Solution
def mark_grade():
  percent_mark = float(input("What's your percentage score? "))
  if percent_mark >= 90 and percent_mark <= 100: 
    grade = "A"
    print(f"You scored {grade} in Coding 101.")

  elif percent_mark >= 80 and percent_mark < 90:
    grade = "B"
    print(f"You scored {grade} in Coding 101.")

  elif percent_mark >= 70 and percent_mark < 80:
    grade = "C"
    print(f"You scored {grade} in Coding 101.")

  elif percent_mark >= 60 and percent_mark < 70:
    grade = "D"
    print(f"You scored {grade} in Coding 101.")
  
  elif percent_mark >= 40 and percent_mark < 60:
    grade = "E"
    print(f"You scored {grade} in Coding 101.")

  elif percent_mark >=0 and percent_mark < 40:
    grade = "F"
    print(f"You scored {grade} in Coding 101.")

  else:
    print("Incorrent score, percentage score must be between 0 and 100. Please enter your correct mark: \n")
    return mark_grade()
    
mark_grade()

    
  
