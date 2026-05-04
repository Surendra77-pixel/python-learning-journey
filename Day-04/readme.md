# 🐍 Python Lists — Complete Study Notes

A complete beginner-to-intermediate guide to Python Lists and Data Structures, organized across 23 Python files.

---

## 📁 File Index

| File | Topic |
|------|-------|
| `0_Datastructures.py` | Overview of all Python Data Structures |
| `01_lists.py` | Introduction to Lists |
| `02_Index.py` | Indexing |
| `03_slicing.py` | Slicing |
| `04_unpacking.py` | Unpacking |
| `05_modifying_lists.py` | Modifying Lists |
| `06_checking_items_in_a_list.py` | Checking Items |
| `07_Adding_items_to_list.py` | Adding Items |
| `08_Removing_items_in_list.py` | Removing Items |
| `09_copying_lists.py` | Copying Lists |
| `10_joinlists.py` | Joining Lists |
| `11_counting_items_in_a_list.py` | Counting Items |
| `12_finding_index_of_an_item.py` | Finding Index |
| `13_reversing_a_list.py` | Reversing a List |
| `14_sorting_the_list_items.py` | Sorting |
| `15_loop_through_list.py` | Looping Through a List |
| `16_list_comprehension.py` | List Comprehension |
| `17_condition.py` | Conditions in Comprehension |
| `18_Iterable.py` | Iterables |
| `19_expression.py` | Expressions |
| `20_list_methods.py` | All List Methods (Reference) |
| `21_list_unpacking` | List Unpacking (Advanced) |
| `list_mini_project.py` | 🛒 Mini Project — Grocery Billing System |

---

## 🗂️ 0. Data Structures Overview

Python has four main built-in data structures:

| Structure | Ordered | Mutable | Duplicates | Syntax |
|-----------|---------|---------|------------|--------|
| **List** | ✅ | ✅ | ✅ | `[1, "a", 3.14]` |
| **Tuple** | ✅ | ❌ | ✅ | `(1, "a", 3.14)` |
| **Set** | ❌ | ✅ | ❌ | `{1, "a", 3.14}` |
| **Dictionary** | ❌ | ✅ | ❌ (keys) | `{"key": "value"}` |

```python
my_list  = [1, "hello", 3.14, True]
my_tuple = (1, "world", 2.71, False)
my_set   = {1, "python", 3.14}
my_dict  = {"name": "surendra", "age": 25}
```

---

## 📋 1. Lists — Introduction

A **list** is an ordered, mutable collection that can hold mixed data types.

```python
# Creating lists
my_list = [1, "hello", 3.14, True]        # square brackets
my_list2 = list([1, "world", 2.71])       # list() constructor
empty_list = []                            # empty list

# Useful operations
print(len(my_list))   # length → 4
print(type(my_list))  # type → <class 'list'>
```

### Key Rules
- ✅ Ordered and indexed (starts at `0`)
- ✅ Mutable — you can add, remove, or change items
- ✅ Allows duplicate values
- ✅ Can store different data types
- ✅ Supports indexing, slicing, looping, and nesting

### Real-World Uses
- Student data management
- Shopping carts in e-commerce
- Game object storage
- API response data
- Machine learning feature storage

---

## 🔢 2. Indexing

Access items using their index position.

```python
fruits = ["apple", "banana", "cherry", "date", "fig"]

# Positive indexing (left to right, starts at 0)
print(fruits[0])   # apple
print(fruits[1])   # banana

# Negative indexing (right to left, starts at -1)
print(fruits[-1])  # fig
print(fruits[-2])  # date

# Finding index with start position
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "orange", "cherry"]
print(fruits.index("cherry", 4))  # 6  ← searches from index 4
```

---

## ✂️ 3. Slicing

Access a portion of a list using `list[start:end:step]`.

```python
fruits = ["apple", "banana", "cherry", "date", "fig"]

print(fruits[1:4])   # ['banana', 'cherry', 'date']
print(fruits[2:])    # ['cherry', 'date', 'fig']   ← from index 2 to end
print(fruits[:3])    # ['apple', 'banana', 'cherry'] ← from start to index 3
print(fruits[:])     # full copy of the list
```

### Slicing with Step
```python
fruits = ["apple","banana","cherry","date","fig","grape","kiwi","lemon","mango","orange"]

print(fruits[::2])    # every 2nd item → ['apple', 'cherry', 'fig', 'kiwi', 'mango']
print(fruits[1::2])   # every 2nd from index 1 → ['banana', 'date', 'grape', 'lemon', 'orange']
print(fruits[1:8:3])  # every 3rd from index 1 to 8 → ['banana', 'date', 'lemon']
```

### Negative Slicing
```python
print(fruits[-4:-1])   # ['lemon', 'mango', 'orange'] ← wait, 'kiwi' to 'orange'
print(fruits[-3:])     # last 3 items
print(fruits[:-3])     # everything except last 3
print(fruits[-1::-1])  # full reverse of list
```

---

## 📦 4. Unpacking

Assign list (or string) elements directly to variables in one line.

```python
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a)  # apple
print(b)  # banana
print(c)  # cherry

# Works on strings too
name = "Surendra"
a, b, c, d, e, f, g, h, i, j = name
print(a)  # S
print(b)  # u
# ... and so on
```

> ⚠️ The number of variables must match the number of elements, otherwise a `ValueError` is raised.

---

## ✏️ 5. Modifying Lists

Since lists are **mutable**, you can change their contents after creation.

```python
fruits = ["apple", "banana", "cherry", "date", "fig"]

# Change a single item
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date', 'fig']

# Change a range of items using slicing
fruits[1:4] = ["blueberry", "grape", "kiwi"]
print(fruits)  # ['apple', 'blueberry', 'grape', 'kiwi', 'fig']

# Insert fewer → list shrinks
fruits[1:4] = ["blueberry"]
print(fruits)  # ['apple', 'blueberry', 'fig']
```

---

## 🔍 6. Checking Items in a List

```python
fruits = ["apple", "banana", "cherry", "date", "fig"]

print("banana" in fruits)      # True
print("grape" in fruits)       # False
print("grape" not in fruits)   # True

# Using .count() — returns 0 if not found
print(fruits.count("banana"))  # 1

# Real-life example
students = ["Ravi", "Priya", "Arun"]
name = input("Enter your name: ")
print("Present" if name in students else "Absent")
```

> ⚡ **Performance tip:** Checking membership in a list is **O(n)**. Use a `set` for faster O(1) lookup.
> ```python
> my_set = {1, 2, 3, 4}
> print(3 in my_set)  # Faster!
> ```

---

## ➕ 7. Adding Items

```python
fruits = ["apple", "banana", "cherry"]

# append() — adds ONE item to the end
fruits.append("date")
# ['apple', 'banana', 'cherry', 'date']

# insert() — adds at a specific index
fruits.insert(1, "blueberry")
# ['apple', 'blueberry', 'banana', 'cherry', 'date']

# extend() — adds multiple items from another iterable
fruits.extend(["fig", "grape"])
# ['apple', 'blueberry', 'banana', 'cherry', 'date', 'fig', 'grape']

# + operator — creates a NEW combined list
more = ["kiwi", "lemon"]
all_fruits = fruits + more
```

| Method | Modifies original | Adds how many |
|--------|------------------|---------------|
| `append()` | ✅ | One item at a time |
| `insert()` | ✅ | One item at a position |
| `extend()` | ✅ | Multiple items |
| `+` operator | ❌ (new list) | Multiple items |

---

## ❌ 8. Removing Items

```python
fruits = ["apple", "banana", "cherry", "date", "fig"]

# remove() — removes first occurrence by VALUE
fruits.remove("banana")
# ['apple', 'cherry', 'date', 'fig']

# pop() — removes by INDEX, returns the removed item
removed = fruits.pop(1)
print(removed)  # cherry

# del — removes by index, returns nothing
del fruits[0]

# clear() — empties the entire list
fruits.clear()
print(fruits)   # []
```

| Method | By | Returns removed item |
|--------|----|----------------------|
| `remove(value)` | Value | ❌ |
| `pop(index)` | Index | ✅ |
| `del list[index]` | Index | ❌ |
| `clear()` | — | ❌ |

---

## 📋 9. Copying Lists

```python
fruits = ["apple", "banana", "cherry"]

# Method 1: .copy()
new_fruits = fruits.copy()

# Method 2: list() constructor
new_fruits = list(fruits)

# Method 3: slicing
new_fruits = fruits[:]
```

> ⚠️ Never use `b = a` to copy — both variables will point to the **same** list in memory!

---

## 🔗 10. Joining Lists

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# + operator (creates new list)
combined = list1 + list2               # [1, 2, 3, 4, 5, 6]

# extend() (modifies list1)
list1.extend(list2)                    # [1, 2, 3, 4, 5, 6]

# Unpacking operator *
combined = [*list1, *list2]            # [1, 2, 3, 4, 5, 6]

# itertools.chain()
import itertools
combined = list(itertools.chain(list1, list2))  # [1, 2, 3, 4, 5, 6]

# Manual loop with append()
for x in list2:
    list1.append(x)
```

---

## 🔢 11. Counting Items

```python
fruits = ["apple", "banana", "cherry", "apple"]

print(len(fruits))           # total items → 4
print(fruits.count("apple")) # occurrences of "apple" → 2

age = [25, 30, 35, 40, 25]
print(age.count(25))         # 2
```

---

## 📍 12. Finding the Index of an Item

```python
fruits = ["apple", "banana", "cherry"]

print(fruits.index("banana"))  # 1
print(fruits.index("grape"))   # ValueError if not found

# Find ALL occurrences using a loop
fruits = ["apple", "banana", "cherry", "banana"]
indices = [i for i in range(len(fruits)) if fruits[i] == "banana"]
print(indices)  # [1, 3]
```

---

## 🔄 13. Reversing a List

```python
fruits = ["apple", "banana", "cherry"]

# Method 1: .reverse() — modifies in place
fruits.reverse()
print(fruits)  # ['cherry', 'banana', 'apple']

# Method 2: slicing — creates new list
reversed_fruits = fruits[::-1]

# Method 3: reversed() — returns an iterator
reversed_fruits = list(reversed(fruits))
```

---

## 🔃 14. Sorting a List

```python
fruits = ["banana", "apple", "cherry"]

# .sort() — modifies original, ascending by default
fruits.sort()
print(fruits)  # ['apple', 'banana', 'cherry']

# sorted() — returns new sorted list
sorted_fruits = sorted(fruits)

# Descending order
fruits.sort(reverse=True)
sorted_desc = sorted(fruits, reverse=True)

# Case-insensitive sort
fruits = ["banana", "Apple", "cherry"]
sorted_ci = sorted(fruits, key=str.lower)
# ['Apple', 'banana', 'cherry']
```

| Method | Modifies Original | Returns New List |
|--------|------------------|-----------------|
| `.sort()` | ✅ | ❌ |
| `sorted()` | ❌ | ✅ |

---

## 🔁 15. Looping Through a List

```python
fruits = ["banana", "apple", "cherry"]

# for loop
for fruit in fruits:
    print(fruit)

# while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Using range() and index
for i in range(len(fruits)):
    print(fruits[i])

# Using list comprehension (inline loop)
[print(fruit) for fruit in fruits]
```

---

## 🧠 16. List Comprehension

A shorter, cleaner way to create a new list from an existing one.

**Syntax:** `[expression for item in iterable if condition]`

```python
# Without comprehension
fruits = ["banana", "apple", "cherry", "date", "fig"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

# With comprehension (same result!)
newlist = [x for x in fruits if "a" in x]
print(newlist)  # ['banana', 'apple', 'date']

# Square numbers
numbers = [1, 2, 3, 4, 5]
squared = [n ** 2 for n in numbers]
print(squared)  # [1, 4, 9, 16, 25]

# Filter short fruits
short_fruits = [f for f in fruits if len(f) <= 5]
print(short_fruits)  # ['apple', 'fig']

# Convert to uppercase
new_fruits = [fruit.upper() for fruit in fruits]
print(new_fruits)  # ['BANANA', 'APPLE', 'CHERRY', 'DATE', 'FIG']
```

---

## 🔽 17. Conditions in Comprehension

The `if` clause acts as a filter — only items that return `True` are included.

```python
fruits = ["banana", "apple", "cherry", "date", "fig"]

# Fruits containing 'a'
[x for x in fruits if "a" in x]       # ['banana', 'apple', 'date']

# Exclude "banana"
[x for x in fruits if x != "banana"]  # ['apple', 'cherry', 'date', 'fig']

# Exclude both "banana" and "apple"
[x for x in fruits if x != "banana" and x != "apple"]  # ['cherry', 'date', 'fig']
```

---

## 🔄 18. Iterables

An **iterable** is any object you can loop over — lists, tuples, strings, generators, etc.

```python
fruits = ["banana", "apple", "cherry"]
for fruit in fruits:
    print(fruit)

# range() is also an iterable
newlist = [x for x in range(10)]
print(newlist)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)    # [0, 2, 4, 6, 8]
```

---

## 💡 19. Expressions

An **expression** is any combination of values, variables, operators, and function calls that evaluates to a result.

```python
# In assignment
x = 2 + 3          # x = 5

# In function argument
def square(n): return n * n
result = square(2 + 3)  # 25

# In control flow
x = 10
if x > 5:
    print("x is greater than 5")

# In list comprehension
numbers = [1, 2, 3, 4, 5]
squared = [n ** 2 for n in numbers]  # [1, 4, 9, 16, 25]
```

---

## 📚 20. All List Methods — Quick Reference

| Method | Description | Example |
|--------|-------------|---------|
| `append(x)` | Add item to end | `lst.append("fig")` |
| `extend(iterable)` | Add all items from iterable | `lst.extend([1,2])` |
| `insert(i, x)` | Insert at index | `lst.insert(1, "x")` |
| `remove(x)` | Remove first occurrence | `lst.remove("apple")` |
| `pop(i)` | Remove & return by index | `lst.pop(0)` |
| `index(x)` | Find first index of value | `lst.index("cherry")` |
| `count(x)` | Count occurrences | `lst.count("apple")` |
| `sort()` | Sort in place | `lst.sort()` |
| `sorted()` | Return new sorted list | `sorted(lst)` |
| `reverse()` | Reverse in place | `lst.reverse()` |
| `clear()` | Remove all items | `lst.clear()` |
| `copy()` | Shallow copy | `lst.copy()` |

---

## 📦 21. List Unpacking (Advanced)

```python
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a)  # apple
print(b)  # banana
print(c)  # cherry
```

> ✅ The number of variables **must exactly match** the number of list elements.

---

## 🛒 Mini Project — Grocery Billing System

A real-world application combining lists, loops, user input, and arithmetic.

```python
items = []
prices = []

print("Welcome to Grocery Billing System")

while True:
    item = input("Enter item (or 'done' to finish): ")
    if item == "done":
        break
    price = float(input("Enter price: "))
    items.append(item)
    prices.append(price)

print("=" * 20)
print("BILL")
print("=" * 20)

total = 0
for i in range(len(items)):
    print(items[i], "=", prices[i])
    total += prices[i]

print("-------------------")
print("Total =", total)
```

**Workflow:** User input → Store in list → Loop → Calculate → Print

**Sample Output:**
```
Enter item: milk    → price: 40
Enter item: bread   → price: 30
Enter item: done

====================
BILL
====================
milk = 40.0
bread = 30.0
-------------------
Total = 70.0
```

---

## 🗺️ Learning Roadmap

```
Lists Basics
    ├── Creating & Indexing
    ├── Slicing & Unpacking
    ├── Modifying (add / remove / change)
    ├── Searching & Counting
    ├── Sorting & Reversing
    ├── Copying & Joining
    ├── Loops & List Comprehension
    │       ├── Conditions
    │       ├── Iterables
    │       └── Expressions
    └── Mini Project 🛒
```

---

## 💡 When to Use a List

| Situation | Use List? |
|-----------|-----------|
| Multiple items in order | ✅ |
| Data that changes over time | ✅ |
| Need to loop through items | ✅ |
| Need to filter or transform data | ✅ |
| Need unique values only | ❌ Use `set` |
| Need key-value pairs | ❌ Use `dict` |
| Data should never change | ❌ Use `tuple` |

---

*Happy Coding! 🚀 — Python Lists Series*