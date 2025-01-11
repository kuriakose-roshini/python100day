student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for things in student_scores:
    if 91 <= student_scores[things] <= 100:
        student_grades[things] = "Outstanding"
    elif 81 <= student_scores[things] <= 90:
        student_grades[things] = "Exceeds Expectations"
    elif 71 <= student_scores[things] <= 80:
        student_grades[things] = "Acceptable"
    else:
        student_grades[things] =  "Fail" 

for key in student_grades:
    print(key)
    print(student_grades[key])
