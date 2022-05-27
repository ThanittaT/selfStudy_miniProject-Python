#____miniProject1-studentGradingProgram

student_scores = {"Mr.Henry": 81,
                  "Miss Ron": 78,
                  "Mr.Hermione": 99,
                  "Mr.Draco": 74,
                  "Mr.Neville": 62
                 }

#--TO DO#1: Create empty dictionary to call student_scores
student_grades = {}

#--TO DO#2: write code to add grade
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"


#--don't change code here!
print(student_grades)


"""
-------Expected Result: -------
{'Mr.Henry': 'Exceeds Expectations', 'Miss Ron': 'Acceptable', 'Mr.Hermione': 'Outstanding', 'Mr.Draco': 'Acceptable', 'Mr.Neville': 'Fail'}

------------------------------
"""
