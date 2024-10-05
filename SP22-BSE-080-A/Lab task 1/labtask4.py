marks = int(input("Enter the marks (1-100): "))

if 0 <= marks < 50:
    grade = 'F'
elif 50 <= marks < 60:
    grade = 'E'
elif 60 <= marks < 70:
    grade = 'D'
elif 70 <= marks < 80:
    grade = 'C'
elif 80 <= marks < 90:
    grade = 'B'
elif 90 <= marks <= 100:
    grade = 'A'
else:
    grade = 'Invalid input'

if grade != 'Invalid input':
    print(f"The grade for {marks} marks is: {grade}")
else:
    print("Please enter valid marks between 1 and 100.")
