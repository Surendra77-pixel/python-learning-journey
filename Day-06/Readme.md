# Day 6 – Python Sets & Tuples

A complete reference guide covering Python **Tuples** and **Sets** — from the basics through advanced operations, methods, operators, and a mini project.

---

## Table of Contents

1. [Tuples](#tuples)
2. [Sets – Basics](#sets--basics)
3. [Sets – CRUD Operations](#sets--crud-operations)
4. [Sets – Looping & Conversion](#sets--looping--conversion)
5. [Sets – Join Operations](#sets--join-operations)
6. [Sets – Intersection](#sets--intersection)
7. [Sets – Difference](#sets--difference)
8. [Sets – Symmetric Difference](#sets--symmetric-difference)
9. [Frozen Sets](#frozen-sets)
10. [Set Functions](#set-functions)
11. [Set Methods Reference](#set-methods-reference)
12. [Set Operators Reference](#set-operators-reference)
13. [Mini Project – Student Course Enrollment](#mini-project--student-course-enrollment)

---

## Tuples

> Files: `01_index.py`, `02_slicing.py`

Tuples are **ordered**, **immutable** sequences in Python.

### Accessing Elements
```python
my_tuple = ("audi", "mustang", "ford", "ferrari", "bmw")

# Positive indexing
print(my_tuple[0])   # audi
print(my_tuple[2])   # ford

# Negative indexing
print(my_tuple[-1])  # bmw
print(my_tuple[-2])  # ferrari

# Finding index of an element
print(my_tuple.index("ford"))  # 2
```

### Slicing
```python
fruits = ("apple", "banana", "cherry", "date", "fig",
          "grape", "kiwi", "lemon", "mango", "orange")

print(fruits[-4:-1])   # ('lemon', 'mango', 'orange')
print(fruits[-3:])     # ('mango', 'orange')
print(fruits[:-3])     # ('apple', ..., 'kiwi')
print(fruits[::-1])    # Reversed tuple
print(fruits[::2])     # Every 2nd element from start
print(fruits[1::2])    # Every 2nd element from index 1
print(fruits[::-2])    # Every 2nd element in reverse
```

---

## Sets – Basics

> File: `0_sets.py`

A **set** is an unordered, unindexed collection of unique items written with `{}`.

### Key Rules
| Rule | Description |
|------|-------------|
| Unique values | Duplicates are removed automatically |
| No indexing/slicing | Sets are unordered and unindexed |
| Mutable | You can add/remove items, but not modify existing ones |
| Immutable items only | Elements must be immutable (str, int, tuple — not list/dict) |
| `{}` is a dict | Use `set()` to create an empty set |

```python
# Creating sets
my_set = {1, "hello", (1, 2, 3)}

# Empty set — must use set(), NOT {}
empty_set = set()

# set() from a string creates a set of characters
set("hello")  # {'h', 'e', 'l', 'o'}

# Combine sets using union (+ is not supported)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # {1, 2, 3, 4, 5}
```

---

## Sets – CRUD Operations

> Files: `03_checking_an_item.py`, `04_Adding_items.py`, `05_Removing_the_items.py`

### Checking Items
```python
my_set = {"apple", "banana", "cherry"}

print("banana" in my_set)      # True
print("grape" in my_set)       # False
print("grape" not in my_set)   # True
```

### Adding Items
```python
my_set = {"apple", "banana", "cherry"}

# add() — single item
my_set.add("date")

# update() — multiple items from any iterable
my_set.update(["elderberry", "fig"])
my_set.update({"grape", "honeydew"})
```

### Removing Items
| Method | Behavior |
|--------|----------|
| `remove(x)` | Removes `x`; raises `KeyError` if not found |
| `discard(x)` | Removes `x`; does nothing if not found |
| `pop()` | Removes and returns an arbitrary item |
| `clear()` | Empties the set |
| `del my_set` | Deletes the set variable entirely |

```python
my_set = {"apple", "banana", "cherry"}

my_set.remove("banana")   # KeyError if missing
my_set.discard("grape")   # Safe — no error
removed = my_set.pop()    # Arbitrary item removed
my_set.clear()            # set()
del my_set                # Variable no longer exists
```

---

## Sets – Looping & Conversion

> Files: `06_Converting_list_to_set.py`, `07_loop_sets.py`

### Converting a List to a Set
```python
my_list = ["apple", "banana", "cherry", "apple"]
my_set = set(my_list)
print(my_set)  # {'apple', 'banana', 'cherry'} — duplicate removed
```

### Looping Through a Set
```python
my_set = {"apple", "banana", "cherry"}

# for loop
for item in my_set:
    print(item)

# while loop (convert to list first for indexing)
my_list = list(my_set)
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
```

---

## Sets – Join Operations

> File: `08_join_sets.py`

| Method / Operator | Modifies Original? | Works with non-sets? |
|-------------------|--------------------|----------------------|
| `union()` | No — returns new set | Yes |
| `update()` | Yes | Yes |
| `\|` operator | No — returns new set | No (sets only) |
| `\|=` operator | Yes | No (sets only) |

```python
st1 = {"apple", "banana", "cherry"}
st2 = {"date", "elderberry", "fig"}

# union() — new set, original unchanged
st3 = st1.union(st2)

# update() — modifies st1 in place
st1.update(st2)

# | operator
st3 = st1 | st2

# |= operator (in-place)
st1 |= st2

# Joining multiple sets
st4 = st1.union(st2, st3)
st4 = st1 | st2 | st3
```

---

## Sets – Intersection

> Files: `09_intersection.py`, `9_1_intersection_update.py`

Returns elements **common to both** sets.

| Method / Operator | Modifies Original? | Works with non-sets? |
|-------------------|--------------------|----------------------|
| `intersection()` | No — returns new set | Yes |
| `intersection_update()` | Yes | Yes |
| `&` operator | No — returns new set | No (sets only) |

```python
st1 = {"apple", "banana", "cherry"}
st2 = {"banana", "cherry", "date"}

# intersection() — new set
st3 = st1.intersection(st2)   # {'banana', 'cherry'}

# & operator
st3 = st1 & st2               # {'banana', 'cherry'}

# intersection_update() — modifies st1 in place
st1.intersection_update(st2)  # st1 is now {'banana', 'cherry'}

# Works with lists too (method only, not &)
st3 = st1.intersection(["banana", "cherry", "date"])
```

---

## Sets – Difference

> Files: `10_Difference.py`, `10_1_Difference_update.py`

Returns elements in the **first set but not in the second**.

| Method / Operator | Modifies Original? | Works with non-sets? |
|-------------------|--------------------|----------------------|
| `difference()` | No — returns new set | Yes |
| `difference_update()` | Yes | Yes |
| `-` operator | No — returns new set | No (sets only) |
| `-=` operator | Yes | No (sets only) |

```python
st1 = {"apple", "banana", "cherry"}
st2 = {"banana", "cherry", "date"}

# difference() — new set
st3 = st1.difference(st2)    # {'apple'}

# - operator
st3 = st1 - st2              # {'apple'}

# difference_update() — modifies st1 in place
st1.difference_update(st2)   # st1 is now {'apple'}

# -= operator (in-place)
st1 -= st2

# Multiple sets
st4 = st1.difference(st2, st3)
st4 = st1 - st2 - st3
```

---

## Sets – Symmetric Difference

> Files: `11_Symmetric_Difference.py`, `11_1_Symmetric_Difference_update.py`

Returns elements in **either set, but not in both**.

| Method / Operator | Modifies Original? | Works with non-sets? |
|-------------------|--------------------|----------------------|
| `symmetric_difference()` | No — returns new set | Yes |
| `symmetric_difference_update()` | Yes | Yes |
| `^` operator | No — returns new set | No (sets only) |

```python
st1 = {"apple", "banana", "cherry"}
st2 = {"banana", "cherry", "date"}

# symmetric_difference() — new set
st3 = st1.symmetric_difference(st2)  # {'apple', 'date'}

# ^ operator
st3 = st1 ^ st2                      # {'apple', 'date'}

# symmetric_difference_update() — modifies st1
st1.symmetric_difference_update(st2)  # st1 is now {'apple', 'date'}

# Equivalent expression: (A\B) ∪ (B\A)
st3 = (st1 - st2).union(st2 - st1)
```

### Quick Comparison — difference vs symmetric_difference
```python
st1 = {"apple", "banana", "cherry"}
st2 = {"banana", "cherry", "date"}

print(st1 - st2)   # {'apple'}          — only from st1
print(st1 ^ st2)   # {'apple', 'date'}  — unique to either set
```

---

## Frozen Sets

> File: `12_Frogen_set.py`

A `frozenset` is an **immutable** version of a set — it supports all read operations but cannot be modified.

```python
# Creating a frozenset
fs = frozenset([1, 2, 3, 4, 5])
print(fs)  # frozenset({1, 2, 3, 4, 5})

# Supports set operations (returns new frozenset)
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

print(fs1.union(fs2))         # frozenset({1, 2, 3, 4, 5})
print(fs1.intersection(fs2))  # frozenset({3})
print(fs1.difference(fs2))    # frozenset({1, 2})

# Can be used as dictionary keys (hashable)
my_dict = {frozenset([1, 2, 3]): "value"}

# Copying
copy_fs = fs1.copy()

# Cannot modify — these raise AttributeError:
# fs.add(6)
# fs.remove(1)
# fs.clear()
```

---

## Set Functions

> File: `13_Set_function.py`

```python
# set() — creates a set from any iterable
set([1, 2, 3, 3, 4])    # {1, 2, 3, 4}
set("hello")             # {'h', 'e', 'l', 'o'}
set(["apple", "apple"])  # {'apple'}

# len() — number of elements
len({1, 2, 3})  # 3

# type() — check type
type({1, 2, 3})  # <class 'set'>

# Membership test
1 in {1, 2, 3}   # True
```

---

## Set Methods Reference

> File: `14_set_methods.py`

| Method | Description |
|--------|-------------|
| `add(x)` | Adds element `x` |
| `remove(x)` | Removes `x`; raises `KeyError` if missing |
| `discard(x)` | Removes `x`; no error if missing |
| `pop()` | Removes and returns an arbitrary element |
| `clear()` | Removes all elements |
| `union(*others)` | Returns new set with all elements |
| `update(*others)` | Adds all elements from others in place |
| `intersection(*others)` | Returns common elements (new set) |
| `intersection_update(*others)` | Keeps only common elements in place |
| `difference(*others)` | Returns elements not in others (new set) |
| `difference_update(*others)` | Removes elements found in others in place |
| `symmetric_difference(other)` | Returns elements unique to either set |
| `symmetric_difference_update(other)` | Updates in place with symmetric difference |
| `isdisjoint(other)` | `True` if no elements in common |
| `issubset(other)` | `True` if all elements are in `other` |
| `issuperset(other)` | `True` if set contains all of `other` |
| `copy()` | Returns a shallow copy |

```python
st1 = {"apple", "banana"}
st2 = {"apple", "banana", "cherry"}

print(st1.issubset(st2))    # True
print(st2.issuperset(st1))  # True
print(st1.isdisjoint({"date", "fig"}))  # True
```

---

## Set Operators Reference

> File: `15_Set_operators.py`

| Operator | Operation | Example |
|----------|-----------|---------|
| `\|` | Union | `st1 \| st2` |
| `\|=` | Union (in-place) | `st1 \|= st2` |
| `&` | Intersection | `st1 & st2` |
| `&=` | Intersection (in-place) | `st1 &= st2` |
| `-` | Difference | `st1 - st2` |
| `-=` | Difference (in-place) | `st1 -= st2` |
| `^` | Symmetric Difference | `st1 ^ st2` |
| `^=` | Symmetric Difference (in-place) | `st1 ^= st2` |

> **Note:** All operators (`|`, `&`, `-`, `^`) work **only with sets**. Use methods like `union()`, `intersection()` etc. when working with lists or other iterables.

---

## Mini Project – Student Course Enrollment

> File: `16_miniproject.py`

A practical demonstration of set operations applied to a real-world student enrollment system.

```python
python_course = {"Surendra", "Kalyani", "Rahul", "Akhil"}
java_course   = {"Rahul", "Akhil", "Sneha", "Vijay"}
ai_course     = {"Surendra", "Sneha", "John"}

# Add a student
python_course.add("Manthri")

# Remove a student
python_course.remove("Kalyani")

# Students in Python OR Java (union)
all_students = python_course.union(java_course)

# Students in BOTH Python AND Java (intersection)
common = python_course.intersection(java_course)

# Students ONLY in Python (difference)
only_python = python_course.difference(java_course)

# Subset / Superset check
ai_course.issubset(python_course)       # False
python_course.issuperset(ai_course)     # False

# Disjoint check — no students in common?
java_course.isdisjoint(ai_course)       # False (Sneha is in both)
```

---

## Summary

```
Tuples      →  Ordered, Immutable, Indexed, Allows duplicates
Sets        →  Unordered, Mutable, No index, Unique values only
Frozensets  →  Unordered, Immutable, No index, Unique values only
```