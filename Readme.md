# 🐍 Python Learning Journey — Surendra Manthri

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Days](https://img.shields.io/badge/Days%20Completed-3-brightgreen)
![Level](https://img.shields.io/badge/Level-Beginner%20→%20Intermediate-blueviolet)
![Projects](https://img.shields.io/badge/Mini%20Projects-6-orange)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

> *"Consistency beats intensity. Every day of learning compounds into mastery."*

---

## 👨‍💻 About This Repository

This repository is a **structured, day-by-day record** of my Python learning journey. Each day covers a focused set of concepts with clean, well-commented code examples, hands-on practice problems, and a mini project that combines everything learned.

---

## 📅 Learning Roadmap

| Day | Topic | Concepts | Mini Project |
|-----|-------|----------|--------------|
| Day 1 | Python Foundations | Variables, Data Types, Strings, Operators | User Information Card |
| Day 2 | Conditional Statements | if/elif/else, match-case, Nested Logic | Smart CLI Assistant |
| Day 3 | Loops | while, for, break, continue, pass | Bank System + ATM + Shopping Cart |
| Day 4 | *(Coming Soon)* | Datastructures | — |

---

## 📁 Repository Structure

```
python-learning-journey/
│
├── Day-01/                          # Python Foundations
│   ├── 01_variables.py
│   ├── 02_Datatypes.py
│   ├── 03_conversions.py
│   ├── 04_inputandoutput.py
│   ├── 05_Strings.py
│   ├── 06_Fstringsandformatstrings.py
│   ├── 07_Stringsmethods.py
│   ├── 08_Escapestrings.py
│   ├── 09_operators.py
│   └── 10_miniproject.py
│
├── Day-02/                          # Conditional Statements
│   ├── 00_intro.py
│   ├── 01_conditionalstatements.py
│   ├── 02_Ifstatement.py
│   ├── 03_elif.py
│   ├── 04_else.py
│   ├── 05_shorthand.py
│   ├── 06_combingmultipleoperators.py
│   ├── 07_nestedifstatements.py
│   ├── 08_pass.py
│   ├── 09_match.py
│   ├── 9_1_matchdefault.py
│   ├── 9_2_matchcombine.py
│   ├── 9_3_Othermethodswithmatch.py
│   └── 10_miniproject.py
│
├── Day-03/                          # Loops
│   ├── 01_Loops.py
│   ├── 02_whileloop.py
│   ├── 03_forloop.py
│   ├── 04_range.py
│   ├── 05_nestedloops.py
│   ├── 06_forinpass.py
│   ├── 07_elseinforloop.py
│   ├── 08_forloopminiproject.py
│   ├── 09_miniproject.py
│   ├── 2_1_whilebreak.py
│   ├── 2_2_whilecontinue.py
│   ├── 2_3pass.py
│   ├── 2_4_whileloopminiproject.py
│   ├── 3_1_forbreak.py
│   └── 3_2_forcontinue.py
│
└── README.md
```

---

---

# 📘 DAY 1 — Python Foundations

> **Goal:** Build a rock-solid understanding of Python's core building blocks.

---

## 🟢 Variables (`01_variables.py`)

Variables are named containers that store data in memory.

**Key concepts covered:**
- Naming rules: no hyphens, no spaces, no leading numbers
- Naming styles: camelCase, PascalCase, snake_case
- Multiple assignment: `x, y, z = 10, 20, 30`
- Single value to multiple variables: `x = y = z = 10`
- Unpacking a collection into individual variables

```python
# Multiple assignment
x, y, z = 10, 20, 30

# Unpacking a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
```

---

## 🔵 Data Types (`02_Datatypes.py`)

Python has a rich set of built-in data types.

| Category | Types |
|----------|-------|
| Numeric | `int`, `float`, `complex` |
| Text | `str` |
| Boolean | `bool` |
| Collections | `list`, `tuple`, `set`, `dict`, `frozenset` |
| Sequence | `range` |
| Binary | `bytes`, `memoryview` |
| Null | `NoneType` |

```python
x = 5             # int
y = 3.14          # float
z = 2 + 3j        # complex
name = "Python"   # str
flag = True       # bool
my_list = [1, 2, 3]
my_dict = {"name": "Surendra", "age": 25}
```

Also covered: `type()` for type-checking, and the `random` module for generating random numbers.

---

## 🟡 Type Conversion (`03_conversions.py`)

**Three forms of type handling:**

- **Implicit conversion** — Python auto-converts types during operations (e.g. `int + float → float`)
- **Explicit casting** — Manual conversion using `int()`, `float()`, `str()`
- **Type checking** — Using `type()` to verify a variable's data type

```python
x = 5
y = float(x)   # 5.0 — explicit cast

z = x + 2.0    # 7.0 — implicit conversion
```

---

## 🟣 Input & Output (`04_inputandoutput.py`)

Getting data from the user and displaying results to the console.

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

---

## 🔴 Strings (`05_Strings.py`)

Strings are immutable sequences of characters. Covered extensively:

- Multi-line strings with triple quotes
- Indexing: `a[0]`, `a[1]`
- Looping through characters with `for`
- `len()` for string length
- `in` and `not in` for substring search
- Slicing: `a[2:5]`, `a[:4]`, `a[5:]`
- Negative indexing: `a[-6:-1]`
- Reversing: `a[::-1]`

```python
a = "The ai is the future"
print(a[0])       # T
print(a[::-1])    # erutuf eht si ia ehT
print(a[-6:])     # future
```

---

## 🟠 F-Strings & Format Strings (`06_Fstringsandformatstrings.py`)

Three ways to format strings in Python:

```python
name = "Surendra"
age = 25

# Modern — f-strings (recommended)
print(f"My name is {name} and I am {age} years old.")

# .format() method
print("My name is {} and I am {} years old.".format(name, age))

# Legacy — % formatting
print("My name is %s and I am %d years old" % (name, age))
```

Also covered: `:.2f` for decimal precision, embedding expressions and functions inside f-strings.

---

## ⚫ String Methods (`07_Stringsmethods.py`)

24 string methods explored with examples:

`upper()`, `lower()`, `strip()`, `lstrip()`, `rstrip()`, `replace()`, `split()`, `capitalize()`, `casefold()`, `center()`, `count()`, `encode()`, `endswith()`, `expandtabs()`, `find()`, `format()`, `isalnum()`, `isalpha()`, `title()`, `startswith()`, `join()`, `isupper()`, `islower()`, and string concatenation with `+`.

```python
a = "  hello world  "
print(a.strip())          # "hello world"
print(a.upper())          # "  HELLO WORLD  "
print(a.replace("hello", "hi"))  # "  hi world  "
```

---

## 🔡 Escape Characters (`08_Escapestrings.py`)

| Escape | Meaning |
|--------|---------|
| `\'` | Single quote |
| `\"` | Double quote |
| `\\` | Backslash |
| `\n` | New line |
| `\t` | Tab |
| `\b` | Backspace |

---

## ⚡ Operators (`09_operators.py`)

All 7 operator types covered in depth:

| Type | Operators |
|------|-----------|
| Arithmetic | `+  -  *  /  %  **  //` |
| Comparison | `==  !=  >  <  >=  <=` |
| Logical | `and  or  not` |
| Assignment | `=  +=  -=  *=  /=  %=  **=  //=` |
| Bitwise | `&  \|  ^  ~  <<  >>` |
| Identity | `is  is not` |
| Membership | `in  not in` |

Also covered: operator **precedence** (parentheses → exponentiation → others) and **associativity** (left to right).

---

## 💻 Day 1 Mini Project — User Information Card (`10_miniproject.py`)

A formatted personal card built using `input()`, f-strings, escape sequences, and operators.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\n" + "="*30)
print("     USER INFORMATION CARD")
print("="*30)
print(f"Name  : {name}")
print(f"Age   : {age}")
print("="*30)
```

**Concepts combined:** input/output, f-strings, string operators, escape characters.

---

---

# 📘 DAY 2 — Conditional Statements & Control Flow

> **Goal:** Teach the program to think and make decisions.

---

## 🔀 What Are Conditional Statements? (`01_conditionalstatements.py`)

Conditional statements allow a program to execute different blocks of code based on whether conditions are true or false.

Two execution types introduced:
- **Conditional execution** — runs code only when a condition is met
- **Repetitive execution** — runs code repeatedly while a condition holds (`while` loop preview)

---

## ✅ `if` Statement (`02_Ifstatement.py`)

10 real-world practice problems solved using `if`:

- Positive / Negative / Zero checker
- Even or Odd number
- Voting eligibility
- Largest of three numbers
- Grade system (A/B/C/Fail)
- Divisibility by 3 and 5
- Leap year checker
- Simple login system
- Number range classifier (Low / Medium / High)
- Triangle type checker (Equilateral / Isosceles / Scalene)
- ATM withdrawal system
- Electricity bill calculator

---

## 🔁 `elif` Statement (`03_elif.py`)

Used to check multiple conditions in sequence. Only the first matching condition executes — the rest are skipped.

```python
score = int(input("Enter score: "))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade F")
```

---

## 🔚 `else` Statement (`04_else.py`)

The `else` block is the fallback — it runs only when all `if` and `elif` conditions are false.

```python
balance = 1000
amount = int(input("Enter amount: "))
if amount > balance:
    print("Insufficient balance")
else:
    print("Transaction successful")
```

---

## ⚡ Shorthand If-Else (`05_shorthand.py`)

Compact one-liner syntax (ternary operator):

```python
# Single condition
print("Positive") if a > 0 else print("Not positive")

# Chained conditions
grade = "C" if score < 60 else "B" if score < 80 else "A"
```

---

## 🔗 Combining Multiple Conditions (`06_combingmultipleoperators.py`)

Using `and`, `or`, `not` to build complex logic:

**Problems solved:**
- Work eligibility (age range check)
- Temperature classifier (Hot / Normal / Cold)
- FizzBuzz (divisibility by 3 and 5)
- Login system with wrong-password vs. user-not-found distinction

```python
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
```

---

## 🪆 Nested If Statements (`07_nestedifstatements.py`)

Conditions inside conditions — for multi-layered decision making.

```python
# Voting + drinking eligibility
if age >= 18:
    print("Eligible to vote")
    if age >= 21:
        print("Also eligible to drink")
    else:
        print("Not eligible to drink")

# Student pass/fail with nested criteria
if score >= 85:
    if attendance >= 90:
        if submitted:
            print("Pass")
```

---

## 🚧 `pass` Statement (`08_pass.py`)

A null placeholder — lets you write a syntactically valid empty block to fill in later.

```python
if age >= 18:
    pass  # logic to be added later
else:
    print("Not eligible")
```

---

## 🎛️ `match-case` Statement (`09_match.py`, `9_1` – `9_3`)

Python 3.10+ pattern matching — a cleaner alternative to long if-elif chains.

**Four files covering:**

| File | Concept |
|------|---------|
| `09_match.py` | Basic match-case syntax, matching with `.split()` |
| `9_1_matchdefault.py` | The `_` wildcard as default fallback |
| `9_2_matchcombine.py` | Matching multiple values with `\|` (pipe) |
| `9_3_Othermethodswithmatch.py` | match + `if` guards, `and`/`or`/`not`, `in`/`not in` |

```python
match command:
    case "start" | "begin":
        print("Starting...")
    case "stop" | "end":
        print("Stopping...")
    case _:
        print("Unknown command")
```

---

## 💻 Day 2 Mini Project — Smart CLI Assistant (`10_miniproject.py`)

A command-line assistant combining all Day 2 concepts:

```
start car       → starts a known vehicle (membership check)
check age 17    → returns Minor / Adult / Senior Citizen
login admin     → nested if for password validation
status 7        → Even or Odd (shorthand if)
update          → pass placeholder for future feature
```

**Concepts combined:** match-case, nested if, logical operators, membership operators, shorthand if, pass.

---

---

# 📘 DAY 3 — Loops

> **Goal:** Make code repeat — efficiently and with full control.

---

## 🔁 Loops Introduction (`01_Loops.py`)

Two types of loops in Python:

- **`while` loop** — repeats as long as a condition is true (condition-driven)
- **`for` loop** — iterates over a sequence a set number of times (sequence-driven)

---

## 🔄 While Loop (`02_whileloop.py`)

Runs while the condition is `True`. Requires an update to avoid infinite loops.

**Examples covered:**
- Print 1 to 5
- Countdown from 10 to 1
- Login system with 3 attempts and account lock
- "Keep eating until full" food input loop
- Password checker — keeps asking until correct
- Game exit loop

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

## ➿ For Loop (`03_forloop.py`)

Iterates over any sequence — range, list, tuple, string, or dictionary.

**8 examples covered:**
- Print 1–5 using `range()`
- Reverse countdown using `range(10, 0, -1)`
- Loop through a list of fruits
- Loop through characters in a string
- Loop through a tuple of numbers
- Loop through a dictionary (keys and values)
- Reverse using `reversed()`
- Square number multiplication table

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

for key, value in person.items():
    print(key, ":", value)
```

---

## 📐 `range()` Function (`04_range.py`)

| Syntax | Effect |
|--------|--------|
| `range(10)` | 0 to 9 |
| `range(1, 11)` | 1 to 10 |
| `range(1, 11, 2)` | 1, 3, 5, 7, 9 |
| `range(10, 0, -1)` | 10 down to 1 |

---

## 🔀 Nested Loops (`05_nestedloops.py`)

An inner loop runs completely for every single iteration of the outer loop.

**Patterns built:**
- Right-angled star triangle
- Full 10×10 multiplication table
- Number triangle (1, 12, 123…)
- All combinations of two lists (adjectives × fruits)

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

---

## 🛑 Loop Control Statements

### `break` — Exit Early

| File | Loop | Example |
|------|------|---------|
| `2_1_whilebreak.py` | while | Exit on correct guess (guessing game) |
| `3_1_forbreak.py` | for | Stop at "cherry" in a fruit list |

```python
for fruit in ["apple", "banana", "cherry", "date"]:
    if fruit == "cherry":
        break
    print(fruit)
# Output: apple, banana
```

### `continue` — Skip an Iteration

| File | Loop | Example |
|------|------|---------|
| `2_2_whilecontinue.py` | while | Print odds 1–20, skip 13 |
| `3_2_forcontinue.py` | for | Skip even numbers, skip "cherry" |

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
# Output: 1 3 5 7 9
```

### `pass` — Do Nothing (Placeholder)

| File | Loop |
|------|------|
| `2_3pass.py` | while |
| `06_forinpass.py` | for |

```python
for _ in range(100):
    pass  # game logic to be filled in later
```

---

## 🔚 `else` in For Loop (`07_elseinforloop.py`)

The `else` block runs after the loop completes **only if no `break` was triggered**.

```python
for i in range(1, 6):
    print(i)
else:
    print("Loop finished normally")  # runs ✅

for i in range(1, 6):
    if i == 3:
        break
else:
    print("This won't print")  # skipped ❌
```

---

## 💻 Day 3 Mini Projects

### 🛒 Shopping Cart (`08_forloopminiproject.py`)

Browse a product list, select items by number, view your cart, and get a total bill — all driven by `for` loops.

```
Available Products:
0 - Shirt ₹ 500
1 - Shoes ₹ 1500
2 - Watch ₹ 2000
3 - Cap ₹ 300

Enter product numbers: 0,2
Total Bill: ₹2500
```

### 🏦 Bank System (`09_miniproject.py`)

A full menu-driven banking app using `while True` with `break` on exit.

Features: balance check, deposit, withdrawal with validation, invalid input handling.

```
--- BANK MENU ---
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
```

### 🏧 ATM Login & Withdrawal (`2_4_whileloopminiproject.py`)

A two-stage system combining login security and banking operations.

- Login: 3 attempts, account lock on failure
- Withdrawal: loop with balance validation, exit on `0`

---

---

## 📈 Overall Learning Outcomes

| Skill | Status |
|-------|--------|
| Python syntax and structure | ✅ Complete |
| All core data types | ✅ Complete |
| String manipulation (24+ methods) | ✅ Complete |
| All 7 operator types | ✅ Complete |
| Conditional logic (if/elif/else) | ✅ Complete |
| Pattern matching with match-case | ✅ Complete |
| Loops (while, for, nested) | ✅ Complete |
| Loop control (break, continue, pass) | ✅ Complete |
| Real-world mini projects | ✅ 6 Built |
| Functions | ⏳ Day 4 |
| Lists & Collections (deep dive) | ⏳ Upcoming |
| File Handling | ⏳ Upcoming |

---

## ⭐ Follow My Journey

Stay tuned as I continue learning and building projects daily!
