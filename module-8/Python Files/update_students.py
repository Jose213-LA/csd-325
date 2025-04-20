import json

# Function to print student list
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# File path
file_path = 'student.json'

# Load the original student data
with open(file_path, 'r') as file:
    students = json.load(file)

print("Original Student List:")
print_students(students)

# Add your own student data
new_student = {
    "F_Name": "Jose",
    "L_Name": "Flores",
    "Student_ID": 99999,
    "Email": "zeak1719@yahoo.com"
}
if new_student not in students:
    students.append(new_student)

print("\nUpdated Student List:")
print_students(students)

# Write the updated student list back to the file
with open(file_path, 'w') as file:
    json.dump(students, file, indent=4)

print("\nThe student.json file was updated.")
