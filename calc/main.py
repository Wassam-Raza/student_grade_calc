name = input("Enter student name: ")
try:
 marks = int(input("Enter student marks: "))
except ValueError:
 print("Error: Marks must be a number.")
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