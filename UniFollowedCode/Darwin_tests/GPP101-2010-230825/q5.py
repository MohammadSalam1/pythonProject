def highest_grade_student(student_info):
    highest_grade = 0
    top_student = []  

    for student in student_info:
        grade = student[2]
        
        if grade > highest_grade:
            highest_grade += grade
            top_student = student[0]

    return top_student

# Test cases
students = [["Alice", 18, 90.5], ["Bob", 19, 85.0], ["Cathy", 20, 92.3], ["David", 21, 90.5]]
print(highest_grade_student(students))  # Output: "Cathy"

other_students = [["Eva", 22, 80.0], ["Frank", 23, 88.5], ["Grace", 24, 88.5], ["Helen", 25, 82.2]]
print(highest_grade_student(other_students))  # Output: "Frank"
