# Exception Handling in Python

A beginner-friendly guide to understanding **Exception Handling in Python** with real-world examples, syntax explanations, and a mini project.

---

# 📚 Topics Covered

1. What is an Exception?
2. `try` Block
3. `except` Block
4. `else` Block
5. `finally` Block
6. `raise` Statement
7. Common Exceptions
8. Custom Exceptions
9. ATM Mini Project
10. Real-Time Examples

---

# 🚨 What is an Exception?

An **exception** is an error that occurs while a program is running.

Without exception handling, programs crash when errors happen.

Example:

```python
print(10 / 0)
```

Output:

```python
ZeroDivisionError: division by zero
```

Python stops the program because dividing by zero is impossible.

---

# ✅ Why Exception Handling is Important

Exception handling helps programs:

- Prevent crashes
- Handle errors gracefully
- Continue execution safely
- Improve user experience

Real-world software like:

- Banking apps
- Instagram
- APIs
- AI systems
- Cloud servers

all use exception handling.

---

# 🔹 try Block

The `try` block contains code that may cause an error.

## Syntax

```python
try:
    risky_code()
```

## Example

```python
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# 🔹 except Block

The `except` block handles the error.

## Example

```python
try:
    print(5 / 0)

except:
    print("Error handled")
```

Output:

```python
Error handled
```

---

# 🔹 Multiple except Blocks

Python checks exceptions from top to bottom.

```python
try:
    num = int(input("Enter number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
```

---

# 🔹 else Block

The `else` block runs only if there is NO exception.

## Example

```python
try:
    num = int("20")
    print(num)

except ValueError:
    print("Error")

else:
    print("Success")
```

Output:

```python
20
Success
```

---

# 🔹 finally Block

The `finally` block always executes whether an error happens or not.

## Example

```python
try:
    print(10 / 2)

except:
    print("Error")

finally:
    print("Always executes")
```

Output:

```python
5.0
Always executes
```

---

# 🔹 raise Statement

`raise` is used to manually create exceptions.

## Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

Output:

```python
ValueError: Age cannot be negative
```

---

# 🔹 Common Exceptions in Python

| Exception | Meaning |
|---|---|
| `SyntaxError` | Wrong syntax |
| `NameError` | Variable not defined |
| `TypeError` | Wrong data type |
| `ValueError` | Invalid value |
| `IndexError` | Invalid list index |
| `KeyError` | Invalid dictionary key |
| `AttributeError` | Invalid attribute |
| `ZeroDivisionError` | Divide by zero |
| `FileNotFoundError` | File not found |
| `ModuleNotFoundError` | Module missing |

---

# 🔹 Custom Exceptions

You can create your own exceptions.

## Syntax

```python
class MyError(Exception):
    pass
```

## Example

```python
class InvalidAgeError(Exception):
    pass

age = -1

if age < 0:
    raise InvalidAgeError("Age cannot be negative")
```

---

# 🏦 ATM Mini Project

This project demonstrates:

- `try`
- `except`
- `else`
- `finally`
- Custom Exception
- Validation

## Code

```python
class InsufficientBalanceError(Exception):
    pass

balance = 5000

try:
    print("Welcome to Python Bank ATM")

    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    if amount > balance:
        raise InsufficientBalanceError("Insufficient Balance")

    balance = balance - amount

except ValueError as e:
    print("Value Error:", e)

except InsufficientBalanceError as e:
    print("Transaction Failed:", e)

else:
    print("Transaction Successful")
    print("Remaining Balance:", balance)

finally:
    print("Thank you for using Python Bank ATM")
```

---

# 🧠 Memory Tricks

| Concept | Memory Trick |
|---|---|
| `try` | Try risky code |
| `except` | Catch errors |
| `else` | Runs if no error |
| `finally` | Always runs |
| `raise` | Create error manually |
| Custom Exception | Your own error type |

---

# 🛠 Real-Time Use Cases

## Banking Systems

- Insufficient balance
- Invalid transactions

## Login Systems

- Wrong password
- Invalid username

## APIs

- Invalid requests
- Authentication failures

## File Handling

- Missing files
- Permission issues

---

# 📌 Key Rules

- Code that may fail goes inside `try`
- Error handling goes inside `except`
- `else` runs only when no error occurs
- `finally` always runs
- One `try` can have multiple `except`
- Generic `except` should be last

---

# 📂 Project Files

| File | Topic |
|---|---|
| `00_Exception.py` | Introduction to Exceptions |
| `01_common exception.py` | Common Exceptions |
| `02_try.py` | `try` Block |
| `03_expect.py` | `except` Block |
| `04_else.py` | `else` Block |
| `05_finally.py` | `finally` Block |
| `06_exception as.py` | `Exception as e` |
| `07_raise.py` | `raise` Statement |
| `08_custom exception.py` | Custom Exceptions |
| `09_miniproject.py` | ATM Mini Project |

---

# 🎯 Conclusion

Exception handling is one of the most important concepts in Python programming.

It helps developers:

- Build stable software
- Prevent crashes
- Handle unexpected situations
- Create professional applications

Mastering exception handling is essential for becoming a strong Python developer.