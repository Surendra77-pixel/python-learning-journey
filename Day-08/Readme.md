# 🐍 Python Functions — Complete Study Notes

> **Today's Task** | Python Functions: Zero to Advanced  
> **Files Covered:** 12 | **Topics:** 12 | **Mini Project:** ✅ Quiz Game

---

## 📋 Table of Contents

- [01 — Functions](#01--functions)
- [02 — Arguments](#02--arguments)
- [03 — Passing Different Datatypes](#03--passing-different-datatypes)
- [04 — Positional-Only Arguments](#04--positional-only-arguments)
- [05 — Keyword-Only Arguments](#05--keyword-only-arguments)
- [06 — Scope & LEGB Rule](#06--scope--legb-rule)
- [07 — Decorators](#07--decorators)
- [08 — Lambda Functions](#08--lambda-functions)
- [09 — Recursion](#09--recursion)
- [10 — Generators](#10--generators)
- [11 — Python Built-in Functions](#11--python-built-in-functions)
- [12 — Mini Project: Quiz Game](#12--mini-project-quiz-game)
- [Quick Reference Cheatsheet](#-quick-reference-cheatsheet)

---

## 01 — Functions

**File:** `01_Functions.py`

A **function** is a reusable block of code that only runs when called. It accepts input (parameters) and can return output.

### ✅ Why Use Functions?

Without functions — repeated code:
```python
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp1 = 95
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)
```

With functions — clean & reusable:
```python
def fahrenheit_to_celsius(temp_f):
    return (temp_f - 32) * 5 / 9

print(fahrenheit_to_celsius(77))   # 25.0
print(fahrenheit_to_celsius(95))   # 35.0
print(fahrenheit_to_celsius(50))   # 10.0
```

### 🔑 Key Syntax
```python
def function_name(parameters):
    # code block
    return result
```

---

## 02 — Arguments

**File:** `02_Arguments.py`

### Types of Arguments

| Type | Description | Example |
|---|---|---|
| **Positional** | Matched by order | `my_func("Alice", 30)` |
| **Keyword** | Matched by name | `my_func(name="Alice", age=30)` |
| **Default** | Used when no value passed | `def my_func(name="surendra")` |
| **Mixed** | Positional before keyword | `my_func("Dog", name="Buddy", age=5)` |

### Parameter vs Argument
```python
def greet(name):        # 'name' is the PARAMETER (placeholder)
    print(f"Hello, {name}!")

greet("Alice")          # "Alice" is the ARGUMENT (actual value)
```

### Default Arguments
```python
def my_function(name="surendra"):
    print("hello", name)

my_function("kiran")    # hello kiran
my_function()           # hello surendra  ← uses default
```

### ⚠️ Rules for Mixing Arguments
```python
# ✅ Valid — positional BEFORE keyword
my_function("Dog", name="Buddy", age=5)

# ❌ Invalid — keyword BEFORE positional → SyntaxError
my_function(name="Buddy", age=5, "Dog")
```

---

## 03 — Passing Different Datatypes

**File:** `03_Passing_different_datatypes.py`

Any Python datatype can be passed as a function argument.

```python
# List
def my_function(names):
    for fruit in names:
        print(fruit)
my_function(["apple", "banana", "orange"])

# Tuple
my_function(("apple", "banana", "orange"))

# Dictionary
def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
my_function({"name": "Alice", "age": 30})

# Set
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_function({"apple", "banana", "orange"})

# String
def my_function(name):
    print("Hello, " + name + "!")
my_function("Alice")
```

### Returning Multiple Datatypes
```python
def my_function():
    return [1, 2, 3], {"name": "Alice"}, (4, 5, 6), "Hello"

result = my_function()
print(result)
# ([1, 2, 3], {'name': 'Alice', 'age': 30}, (4, 5, 6), 'Hello')
```

---

## 04 — Positional-Only Arguments

**File:** `04_positional-only_arg.py`

Use `/` after parameters to make them **positional-only** — keyword syntax is not allowed for these.

```python
def my_function(name, age, /):
    print(f"my name is {name} and my age is {age}")

my_function("surendra", "20")          # ✅ Works
my_function(name="surendra", age="20") # ❌ TypeError
```

### Comparison Table

| Type | Syntax | Positional Call | Keyword Call |
|---|---|---|---|
| Normal | `def f(a, b)` | ✅ | ✅ |
| Positional-only | `def f(a, b, /)` | ✅ | ❌ |

---

## 05 — Keyword-Only Arguments

**File:** `05_Keyword-only_arg.py`

Use `*` before parameters to make them **keyword-only** — positional syntax is not allowed for these.

```python
def my_function(*, name, age):
    print(f"my name is {name} and my age is {age}")

my_function(name="surendra", age="20") # ✅ Works
my_function("surendra", "20")          # ❌ TypeError
```

### Combining Both — Positional-Only + Keyword-Only
```python
def my_function(positional_arg, *, keyword_arg):
    print(f"Positional argument: {positional_arg}")
    print(f"Keyword argument: {keyword_arg}")

my_function("positional value", keyword_arg="keyword value")
# Positional argument: positional value
# Keyword argument: keyword value
```

### Full Argument Type Cheatsheet

| Symbol | Meaning |
|---|---|
| `def f(a, b)` | Normal — positional or keyword |
| `def f(a, b, /)` | Before `/` = positional-only |
| `def f(*, a, b)` | After `*` = keyword-only |
| `def f(a, /, b, *, c)` | Mixed — all three together |

---

## 06 — Scope & LEGB Rule

**File:** `06_Scope.py`

**Scope** defines where a variable is accessible. Python uses the **LEGB** rule to resolve variable names.

```
L → Local       (inside current function)
E → Enclosing   (inside outer/enclosing function)
G → Global      (top level of the script/module)
B → Built-in    (Python's built-in names like len, print)
```

### The Four Scopes

```python
# 1️⃣ LOCAL
def my_function():
    x = 10          # local — only inside this function
    print(x)

# 2️⃣ ENCLOSING
def outer_function():
    x = 20
    def inner_function():
        print(x)    # accesses enclosing scope
    inner_function()

# 3️⃣ GLOBAL
y = 30
def another_function():
    print(y)        # accesses global variable

# 4️⃣ BUILT-IN
print(len("Hello"))  # len is from built-in scope
```

### `global` Keyword
```python
x = 100
def my_func():
    global x        # modify the global variable
    x = 200
my_func()
print(x)            # 200
```

### `nonlocal` Keyword
```python
def outer_func():
    x = 100
    def inner_func():
        nonlocal x  # modify enclosing scope variable
        x = 200
    inner_func()
    print(x)        # 200
```

---

## 07 — Decorators

**File:** `07_Decorators.py`

A **decorator** is a higher-order function that wraps another function to modify its behavior — without changing its source code.

```python
def change_case(func):
    def myinner():
        return func().upper()
    return myinner

@change_case
def my_function():
    return "hello, world!"

print(my_function())  # HELLO, WORLD!
```

### Applying to Multiple Functions
```python
@change_case
def my_function():
    return "hello, world!"

@change_case
def another_function():
    return "python is great!"

print(my_function())      # HELLO, WORLD!
print(another_function()) # PYTHON IS GREAT!
```

### How It Works
```
@change_case          is shorthand for:
def my_function():    →   my_function = change_case(my_function)
    ...
```

---

## 08 — Lambda Functions

**File:** `08_Lambda.py`

A **lambda** is a small, anonymous, single-expression function.

```python
# Syntax
lambda arguments: expression

# Examples
add    = lambda x, y: x + y        # add(5, 3)   → 8
square = lambda x: x ** 2          # square(4)   → 16
is_even = lambda x: x % 2 == 0     # is_even(6)  → True
```

### Used with Built-in Functions

```python
numbers = [1, 2, 3, 4, 5, 6]

# map() — transform each element
squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25, 36]

# filter() — keep matching elements
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]

# sorted() — custom sort key
my_list = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
sorted_list = sorted(my_list, key=lambda x: x[1])
# [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

# reduce() — rolling computation
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
# 120
```

### Lambda Returning Lambda (Closure)
```python
def my_func(n):
    return lambda a: a * n

my_doubler = my_func(2)
my_tripler = my_func(3)

print(my_doubler(11))   # 22
print(my_tripler(11))   # 33
```

---

## 09 — Recursion

**File:** `09_recursion.py`

**Recursion** is when a function calls itself to solve a problem. Every recursive function needs:

1. **Base Case** — stops the recursion
2. **Recursive Case** — breaks the problem smaller

```python
def count_down(n):
    if n <= 0:          # Base case
        print("Done!")
    else:               # Recursive case
        print(n)
        count_down(n - 1)

count_down(5)  # 5 4 3 2 1 Done!
```

### Classic Recursion Examples

**Factorial:**
```python
def factorial(n):
    if n == 1:                      # Base case
        return 1
    return n * factorial(n - 1)    # Recursive case

print(factorial(5))  # 120
```

**Fibonacci:**
```python
def fibonacci(n):
    if n <= 0:   return 0
    elif n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 55
```

**Sum of a List:**
```python
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15
```

**Find Max in a List:**
```python
def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

print(find_max([3, 5, 2, 8, 1]))  # 8
```

> ⚠️ **Warning:** Always define a base case. Without it, recursion runs forever and causes a `RecursionError`.

---

## 10 — Generators

**File:** `10_Generators.py`

A **generator** produces values one at a time using `yield`, instead of returning everything at once. This saves memory.

### Normal Function vs Generator
```python
# Normal — stores entire list in memory
def normal_function():
    return [1, 2, 3]

# Generator — produces one value at a time
def generator_function():
    yield 1
    yield 2
    yield 3
```

### Using a Generator
```python
def simple_gen():
    yield 'Hello'
    yield 'World'
    yield 'Python'

# Using a for loop
for word in simple_gen():
    print(word)

# Using next()
gen = simple_gen()
print(next(gen))  # Hello
print(next(gen))  # World
print(next(gen))  # Python
print(next(gen))  # ❌ StopIteration
```

### Memory Efficiency
```python
# Generates 1,000,000 numbers without storing all in RAM
def large_sequence(n):
    for i in range(n):
        yield i

gen = large_sequence(1000000)
print(next(gen))  # 0
print(next(gen))  # 1
```

### Generator Expression vs List Comprehension
```python
list_comp = [x * x for x in range(5)]   # Creates full list in memory
gen_exp   = (x * x for x in range(5))   # Lazy — produces one at a time

print(sum(gen_exp))  # 30
```

### Fibonacci Generator
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)  # 0 1 1 2 3 5 8 13 21 34
```

### Generator Methods

| Method | Purpose |
|---|---|
| `next(gen)` | Get the next yielded value |
| `gen.send(value)` | Send a value into the generator |
| `gen.close()` | Stop the generator (raises `GeneratorExit`) |
| `gen.throw(Error)` | Raise an exception inside the generator |

---

## 11 — Python Built-in Functions

**File:** `11_python_functions.py`

| Function | Purpose | Example |
|---|---|---|
| `breakpoint()` | Pause execution for debugging | `breakpoint()` |
| `compile()` | Compile source string to code object | `compile(src, '<string>', 'exec')` |
| `exec()` | Execute a string of Python code | `exec("print('hi')")` |
| `eval()` | Evaluate a Python expression string | `eval("2 + 3 * 4")` → `14` |
| `vars()` | Return object's `__dict__` | `vars(my_object)` |
| `globals()` | Return global symbol table dict | `globals()["x"]` |
| `locals()` | Return local symbol table dict | `locals()` |
| `dir()` | List attributes/methods of an object | `dir(my_list)` |
| `help()` | Show documentation for an object | `help(list)` |
| `callable()` | Check if object is callable | `callable(my_func)` → `True` |

```python
# eval
result = eval("2 + 3 * 4")
print(result)  # 14

# vars
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = MyClass("Alice", 30)
print(vars(obj))  # {'name': 'Alice', 'age': 30}

# callable
def my_function(): pass
print(callable(my_function))  # True
print(callable(10))           # False
```

---

## 12 — Mini Project: Quiz Game

**File:** `12_Miniproject.py`

A fully functional **command-line Quiz Game** built using all the function concepts learned today.

### Features
- 5 multiple-choice questions
- Score tracking with pass/fail result
- Percentage calculation
- Replay functionality

### Project Structure

```
Quiz Game
├── get_questions()   → Returns list of question dictionaries
├── run_quiz()        → Loops through questions, takes input, scores
├── show_result()     → Displays score, percentage, pass/fail
└── main()            → Entry point with replay loop
```

### Code Overview
```python
def get_questions():
    return [ { "question": "...", "options": [...], "answer": "B" }, ... ]

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, start=1):
        # display question → take input → check answer → update score
    return score

def show_result(score, total):
    percentage = (score / total) * 100
    # Print score, percentage, PASS or FAIL

def main():
    questions = get_questions()
    while True:
        score = run_quiz(questions)
        show_result(score, len(questions))
        replay = input("Do you want to play again? (yes/no): ")
        if replay != "yes":
            break

if __name__ == "__main__":
    main()
```

### Sample Output
```
 Question 1: What is the capital of India?
A. Mumbai
B. Delhi
C. Chennai
D. Kolkata
 Enter your answer (A/B/C/D): B
 Correct!

 ===== RESULT =====
Score: 4/5
Percentage: 80.00%
 PASS
```

---

## ⚡ Quick Reference Cheatsheet

```python
# ── FUNCTION BASICS ──────────────────────────────────────
def greet(name="World"):           # default argument
    return f"Hello, {name}!"

# ── ARGUMENT TYPES ───────────────────────────────────────
def f(pos_only, /, normal, *, kw_only):
    pass
#           /  → everything before is positional-only
#           *  → everything after is keyword-only

# ── LAMBDA ───────────────────────────────────────────────
square = lambda x: x ** 2
evens  = list(filter(lambda x: x % 2 == 0, [1,2,3,4]))

# ── SCOPE (LEGB) ──────────────────────────────────────────
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"   # local wins
        print(x)

# ── DECORATOR ────────────────────────────────────────────
def my_dec(func):
    def wrapper(): return func().upper()
    return wrapper

@my_dec
def hello(): return "hello"   # → "HELLO"

# ── RECURSION ────────────────────────────────────────────
def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)

# ── GENERATOR ────────────────────────────────────────────
def count_up(n):
    for i in range(n):
        yield i

gen = count_up(3)
next(gen)  # 0 → 1 → 2
```

---

## 📁 File Index

| # | File | Topic |
|---|---|---|
| 01 | `01_Functions.py` | Function basics, why use functions |
| 02 | `02_Arguments.py` | Positional, keyword, default, mixed args |
| 03 | `03_Passing_different_datatypes.py` | Lists, tuples, dicts, sets, strings as args |
| 04 | `04_positional-only_arg.py` | `/` syntax, positional-only enforcement |
| 05 | `05_Keyword-only_arg.py` | `*` syntax, keyword-only enforcement |
| 06 | `06_Scope.py` | LEGB rule, global/nonlocal keywords |
| 07 | `07_Decorators.py` | Decorator pattern, `@` syntax |
| 08 | `08_Lambda.py` | Lambda, map, filter, reduce, sorted |
| 09 | `09_recursion.py` | Base case, recursive case, factorial, Fibonacci |
| 10 | `10_Generators.py` | yield, next(), send(), close(), throw() |
| 11 | `11_python_functions.py` | Built-ins: eval, exec, vars, dir, help, callable |
| 12 | `12_Miniproject.py` | Quiz Game — all concepts applied |

---

*Completed on: May 2, 2026 | Language: Python 3.x*