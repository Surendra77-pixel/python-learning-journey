

#student record system- we store student data using the tuples because the tuples are immutable

#each student will have name , age , marks

#Concept Understanding- Think of a tuple like a sealed ID card 
#Once created → you cannot change it.
#So each student record = permanent entry.

# Student Record System using Tuples

# Step 1: Create student records (tuples)
student1 = ("Surendra", 20, 85)
student2 = ("praveen", 21, 90)
student3 = ("Vardhan", 19, 78)

# Step 2: Store all students in a tuple
students = (student1, student2, student3)

# Step 3: Display all students
print("----- Student Records -----")
for student in students:
    print("Name:", student[0])
    print("Age:", student[1])
    print("Marks:", student[2])
    print("--------------------------")

# Step 4: Find Topper
topper = students[0]

for student in students:
    if student[2] > topper[2]:
        topper = student

print("\n Topper:")
print(topper[0], "with marks", topper[2])

# Step 5: Calculate Average Marks
total = 0

for student in students:
    total += student[2]

average = total / len(students)
print("\n Average Marks:", average)

# Step 6: Search Student by Name
search_name = input("\nEnter student name to search: ")

found = False
for student in students:
    if student[0].lower() == search_name.lower():
        print("\nStudent Found:")
        print("Name:", student[0])
        print("Age:", student[1])
        print("Marks:", student[2])
        found = True
        break

if not found:
    print("\n Student not found")

# Step 7: Count students above 80 marks
count = 0
for student in students:
    if student[2] > 80:
        count += 1

print("\n Students scoring above 80:", count)

#output:
#----- Student Records -----
#Name: Surendra
#Age: 20
#Marks: 85
#--------------------------
#Name: praveen
#Age: 21
#Marks: 90
#--------------------------
#Name: Vardhan
#Age: 19
#Marks: 78
# Topper:
#praveen with marks 90
# Average Marks: 84.33333333333333
#Enter student name to search: Surendra
#Student Found:
#Name: Surendra
#Age: 20
#Marks: 85
# Students scoring above 80: 2

#In this miniproject, we have created a simple student record system using tuples. We have stored student data in tuples and performed various operations such as finding the topper, calculating average marks, searching for a student by name, and counting students scoring above a certain threshold. The use of tuples ensures that the student records are immutable and cannot be changed once created, making it a suitable choice for storing fixed data like student information.