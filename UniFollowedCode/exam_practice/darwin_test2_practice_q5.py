def highest_grade_student(student_info):
  highest_grade = 0
  highest_grade_student = ""
  for i in student_info:
    if i[2] > highest_grade:
      highest_grade = i[2]
      highest_grade_student = i[0]
  return highest_grade_student

    
    

students = [["Alice", 18, 90.5], ["Bob", 19, 85.0], ["Cathy", 20, 92.3], ["David", 21, 90.5]]
print(highest_grade_student(students)) #Output:"Cathy"

other_students = [["Eva", 22, 80.0], ["Frank", 23, 88.5], ["Grace", 24, 88.5], ["Helen", 25, 82.2]]
print(highest_grade_student(other_students)) #Output:"Frank"