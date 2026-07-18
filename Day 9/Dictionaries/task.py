# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again."
# }
#
# print(programming_dictionary["Bug"])
#
# programming_dictionary["Bug"] = "A moth in your computer."
#
# print(programming_dictionary["Bug"])
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    grade = ''
    score = student_scores[student]
    if score > 90:
        grade = 'Outstanding'
    elif score > 80:
        grade = 'Exceeds Expectations'
    elif score > 69:
        grade = 'Acceptable'
    else:
        grade = 'Fail'
    student_grades[student] = grade

print(student_grades)
print(student_grades['Harry'])