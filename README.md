# 🚀 Python Day 1 – Complete Foundations

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Progress-Day%201-brightgreen)
![Focus](https://img.shields.io/badge/Focus-Fundamentals-orange)
![Level](https://img.shields.io/badge/Level-Beginner-blueviolet)

---

## 📌 Overview

This repository documents my **Day 1 journey in Python programming**, where I focused on building a **strong foundation in core concepts**.

It includes:

* Cleanly structured Python scripts
* Concept explanations
* Hands-on mini project

---

## 🧠 Concepts Covered

### 🟢 Variables

* Store data in memory
* Naming rules & best practices
* Multiple assignments & unpacking

```python
x, y, z = 10, 20, 30
```

---

### 🔵 Data Types

* Numeric → `int`, `float`, `complex`
* Text → `str`
* Collections → `list`, `tuple`, `set`, `dict`
* Boolean → `True/False`

```python
x = 5
y = "Hello"
z = 3.14
```

---

### 🟡 Type Conversion

* Implicit conversion
* Explicit casting using `int()`, `float()`, `str()`

```python
x = 5
y = float(x)
```

---

### 🟣 Input & Output

* Taking user input
* Displaying formatted output

```python
name = input("Enter your name: ")
print("Hello", name)
```

---

### 🔴 Strings

* Immutable sequences
* Indexing & slicing
* Reverse & negative indexing

```python
a = "Python"
print(a[::-1])
```

---

### 🟠 String Methods

* Case conversion → `upper()`, `lower()`
* Cleaning → `strip()`
* Searching → `find()`, `count()`
* Transformation → `replace()`, `split()`

```python
a = "hello"
print(a.upper())
```

---

### ⚫ Escape Characters

* `\n` → New line
* `\t` → Tab
* `\\` → Backslash

```python
print("Hello\nWorld")
```

---

### ⚡ Operators

* Arithmetic → `+ - * / %`
* Comparison → `== != > <`
* Logical → `and or not`
* Assignment → `+= -=`
* Membership → `in`

```python
a = 10
b = 5
print(a + b)
```

---

### 🧩 String Formatting

* f-strings (modern & recommended)
* `.format()` method
* `%` formatting (legacy)

```python
name = "Surendra"
print(f"My name is {name}")
```

---

## 💻 Mini Project – User Information Card

### 🎯 Objective

Create a formatted user card using:

* Input
* f-strings
* Escape sequences
* Operators

### 🧪 Sample Code

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
hobby = input("Enter your hobby: ")

print("\n" + "="*30)
print("     USER INFORMATION CARD")
print("="*30)
print(f"Name  : {name}")
print(f"Age   : {age}")
print(f"City  : {city}")
print(f"Hobby : {hobby}")
print("="*30)
```

---

## 📁 Project Structure

```
python-day1/
│
├── 01_variables.py
├── 02_datatypes.py
├── 03_conversions.py
├── 04_inputandoutput.py
├── 05_strings.py
├── 06_fstrings_formatting.py
├── 07_string_methods.py
├── 08_escape_strings.py
├── 09_operators.py
├── 10_miniproject.py
│
└── README.md
```

---

## 📈 Learning Outcomes

✔ Strong understanding of Python basics
✔ Ability to write clean and readable code
✔ Hands-on experience with string manipulation
✔ Built a real mini project combining concepts

---

## 🔥 What's Next?

* Conditional Statements (`if-else`)
* Loops (`for`, `while`)
* Functions

---

## 👨‍💻 Author

**Surendra Manthri**
🎯 Aspiring Full Stack Developer
💡 Currently learning Python, Web Development & AI

---

## ⭐ Support

If you like this project:

* ⭐ Star this repository
* 🍴 Fork it
* 📢 Share with others

---

> 💬 *“Consistency beats intensity. Day 1 done — many more to go if you are the beginer i suggest you to follow this rodmap for understanding the basics!”*
