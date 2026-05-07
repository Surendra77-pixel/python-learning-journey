# Mini Project: Student Course Enrollment System

# Creating sets for courses
python_course = {"Surendra", "Kalyani", "Rahul", "Akhil"}
java_course = {"Rahul", "Akhil", "Sneha", "Vijay"}
ai_course = {"Surendra", "Sneha", "John"}

# 1️Add a new student
print("Before adding:", python_course)
python_course.add("Manthri")
print("After adding:", python_course)

# 2 Remove a student
python_course.remove("Kalyani")
print("After removing:", python_course)

# 3️ Students in either Python OR Java
all_students = python_course.union(java_course)
print("\nStudents in Python or Java:", all_students)

# 4️ Students in BOTH Python AND Java
common_students = python_course.intersection(java_course)
print("Students in both Python and Java:", common_students)

# 5️ Students only in Python (not in Java)
only_python = python_course.difference(java_course)
print("Students only in Python:", only_python)

# 6️ Check subset
print("\nIs AI course a subset of Python?", ai_course.issubset(python_course))

# 7️ Check superset
print("Is Python a superset of AI?", python_course.issuperset(ai_course))

# 8️ Check if no common students
print("Are Java and AI disjoint?", java_course.isdisjoint(ai_course))

#output:

#Before adding: {'Surendra', 'Rahul', 'Kalyani', 'Akhil'}
#After adding: {'Surendra', 'Rahul', 'Kalyani', 'Akhil', 'Manthri'}
#After removing: {'Surendra', 'Rahul', 'Akhil', 'Manthri'}
#Students in Python or Java: {'Surendra', 'Rahul', 'Akhil', 'Manthri', 'Sneha', 'Vijay'}
#Students in both Python and Java: {'Rahul', 'Akhil'}
#Students only in Python: {'Surendra', 'Manthri'}
#Is AI course a subset of Python? False
#Is Python a superset of AI? False
#Are Java and AI disjoint? False (because both courses have the student "Sneha" enrolled, which means they are not disjoint sets. Disjoint sets have no elements in common, but in this case, "Sneha" is a common element between the Java and AI courses.)
#Note: The output may vary based on the order of elements in the sets, as sets do not maintain a specific order.

#In this mini project, we created a student course enrollment system using sets in Python. We performed various operations such as adding and removing students, finding students enrolled in either or both courses, and checking subset and superset relationships between courses. This project demonstrates the practical use of sets for managing collections of unique items, such as student names in different courses.