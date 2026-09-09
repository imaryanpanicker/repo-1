# This program is to take input from the user for marks scored, and then give output on what grade the marks fall into.

name = input("Enter the name of the person: ")
marks = float(input("Enter the number of marks scored: "))

if marks >= 90 and marks <= 100:
                grade = "A"
elif marks >= 80 and marks < 90:
                grade = "B"
elif marks >= 70 and marks < 80:
                grade = "C"
else:
                grade = "ungraded"

print(f"{name} has been graded: ", grade)
              
