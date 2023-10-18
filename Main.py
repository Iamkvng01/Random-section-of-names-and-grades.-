import random

# Load lists of names from files
maleFirstNames = open("male-first-names.txt", "r").read().splitlines()
femaleFirstName = open("female-first-names-1.txt", "r").read().splitlines()
lastName = open("last-names.txt", "r").read().splitlines()

# Choose a random gender
gender = random.choice(["male", "female"])

# Choose a random first name based on gender
if gender == "male":
    firstName = random.choice(maleFirstNames)
else:
    firstName = random.choice(femaleFirstName)

# Choose a random last name
ranLast = random.choice(lastName)

# Generate a full name
fullName = f"{firstName} {ranLast}"

# Generate a random year between 2019 and 2029
startingYear = 2019
endingYear = 2029
Year = random.randint(startingYear, endingYear)

# List of courses
courses = ["MAT112", "CPE123", "GST104", "MAT221", "CPI109", "CPT342", "EET124", "AET214"]

# Dictionary to map grades to grade points
Grades = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}

# Initialize dictionaries to store course grades and credit units
course_grades = {}
course_units = {}

# Randomly assign grades to each course and credit units
for course in courses:
    course_grades[course] = random.choice(list(Grades.keys()))
    course_units[course] = random.randint(1, 3)

# Calculate total credit load and total credit units
total_credit_load = sum(Grades[course_grades[course]] * course_units[course] for course in courses)
total_credit_units = sum(course_units[course] for course in courses)

# Calculate GPA based on the provided formula
gpa = total_credit_load / total_credit_units if total_credit_units > 0 else 0

# Print student information
print("Name:", fullName)
print("\nGender:", gender.capitalize())
print("\nYear:", Year)
print("\n========  =====  ============\nCOURSE    GRADE   CREDIT UNIT\n========  =====  ============")
for course in courses:
    print(f"{course}\t  {course_grades[course]}\t            {course_units[course]}")
print("========  =======  ===========")
print("\nTOTAL CREDIT LOAD:", total_credit_load)  # Fixed total credit load
print("\nGPA: {:.2f}".format(gpa))  # Display GPA with 2 decimal places

# Determine the student's remark
if 2.50 <= gpa < 3.50:
    remark = "Good"
elif 3.50 <= gpa < 4.50:
    remark = "Very Good"
elif gpa >= 4.50:
    remark = "Excellent"
else:
    remark = "Poor"

print("\nREMARK:", remark)
