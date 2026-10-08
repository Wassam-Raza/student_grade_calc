from logger import logger
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from student_project import validate_name
from student_project import validate_marks

logger.info("Application started")
name = input("Enter student name: ")
if not validate_name(name):
    logger.warning("Empty student name entered")
    print("Error: Name cannot be empty.")
    exit()
try:
    marks = int(input("Enter student marks: "))
except ValueError:
    logger.error("Invalid marks entered")
    print("Error: Marks must be a number.")
    exit()
if not validate_marks(marks):
    logger.warning(f"Invalid marks entered: {marks}")
    print("Error: Marks must be between 0 and 100.")
    exit()
if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"
print()
print("Student Report")
print("----------------")
print(f"Name: {name}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")
