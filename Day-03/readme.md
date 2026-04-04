# 🐍 Python Loops – Complete Learning Guide

A structured collection of Python files covering loops from the basics to real-world mini projects.

---

## 📁 File Structure

```
📂 Python Loops
│
├── 01_Loops.py                  # Introduction to loops
├── 02_whileloop.py              # While loop – syntax & examples
├── 03_forloop.py                # For loop – syntax & examples
├── 04_range.py                  # range() function deep dive
├── 05_nestedloops.py            # Nested loops & patterns
├── 06_forinpass.py              # pass statement in for loops
├── 07_elseinforloop.py          # else clause in for loops
├── 08_forloopminiproject.py     # 🛒 Shopping Cart mini project
├── 09_miniproject.py            # 🏦 Bank System mini project
│
├── 2_1_whilebreak.py            # break in while loops
├── 2_2_whilecontinue.py         # continue in while loops
├── 2_3pass.py                   # pass in while loops
├── 2_4_whileloopminiproject.py  # 🏧 ATM Login & Withdrawal mini project
│
├── 3_1_forbreak.py              # break in for loops
└── 3_2_forcontinue.py           # continue in for loops
```

---

## 📚 Topics Covered

### 🔁 While Loop (`02_whileloop.py`)
- Basic syntax and usage
- Countdown loops
- User login system with max attempts
- Real-world password checker
- Exit conditions using logical operators

### 🔄 For Loop (`03_forloop.py`)
- Iterating over ranges, lists, tuples, strings, and dictionaries
- Reverse iteration using `reversed()`
- Multiplication / square number patterns

### 📐 range() Function (`04_range.py`)
- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`
- Reverse sequences with negative step

### 🔀 Nested Loops (`05_nestedloops.py`)
- Star pattern printing
- Full 10×10 multiplication table
- Number triangle pattern
- Combining lists with nested iteration

### 🛑 Loop Control Statements

| Statement | File(s) | Purpose |
|-----------|---------|---------|
| `break` | `2_1_whilebreak.py`, `3_1_forbreak.py` | Exit a loop early |
| `continue` | `2_2_whilecontinue.py`, `3_2_forcontinue.py` | Skip current iteration |
| `pass` | `2_3pass.py`, `06_forinpass.py` | Placeholder for future code |

### 🔚 else in For Loop (`07_elseinforloop.py`)
- Runs after a loop completes normally
- Skipped when the loop exits via `break`

---

## 🚀 Mini Projects

### 🛒 Shopping Cart (`08_forloopminiproject.py`)
Browse a product list, select items by number, and get a total bill — built entirely using for loops.

### 🏦 Bank System (`09_miniproject.py`)
A menu-driven banking app supporting:
- Balance check
- Deposit
- Withdrawal with validation
- Safe exit

### 🏧 ATM Login & Withdrawal (`2_4_whileloopminiproject.py`)
A combined system featuring:
- Password login with 3 attempts
- Account lock on failure
- Withdrawal loop with balance validation

---

## 🧠 Key Concepts at a Glance

```python
# While loop
while condition:
    # runs while condition is True

# For loop
for item in sequence:
    # runs for each item

# break – exit immediately
# continue – skip to next iteration
# pass – do nothing (placeholder)

# else in loop – runs if no break occurred
for i in range(5):
    ...
else:
    print("Done!")
```

---

## ▶️ How to Run

Make sure Python 3 is installed, then run any file with:

```bash
python filename.py
```

Example:
```bash
python 09_miniproject.py
```

---

## 👨‍💻 Author

**Surendra Manthri**  
Python learner building real-world projects one loop at a time. 🚀