# 📁 Day 12 - Python File Handling

## 📌 Overview

This folder contains all the concepts and examples related to **Python File Handling**.  
File handling is used to store, read, update, and manage data permanently using files.

This day covers:

- File Handling Basics
- File Modes
- Reading Files
- Writing Files
- Appending Data
- Updating Files
- Deleting Files
- Renaming Files
- CSV Module
- JSON Module
- Text vs Binary Files
- With Statement
- Exception Handling

---

# 📚 Topics Covered

---

## 1️⃣ File Handling Introduction

📄 File: `00_file handling.py`

### Concepts:
- What is file handling
- Why file handling is important
- Real-world examples
- File operations
- File modes

### Operations:
- Open
- Read
- Write
- Append
- Update
- Delete
- Rename
- Close

---

## 2️⃣ File Modes

📄 File: `01_file mode.py`

### Modes Covered:

| Mode | Meaning |
|---|---|
| r | Read |
| w | Write |
| a | Append |
| x | Create |
| b | Binary |
| t | Text |
| r+ | Read + Write |
| w+ | Write + Read |
| a+ | Append + Read |

---

## 3️⃣ Open Function

📄 File: `02_open.py`

### Concepts:
- `open()` function
- Opening files
- Relative path
- Absolute path
- Using modes with open()

### Example:
```python
file = open("demo.txt", "r")
```

---

## 4️⃣ Reading Files

📄 File: `03_read.py`

### Methods:
- `read()`
- `readline()`
- `readlines()`

### Example:
```python
with open("demo.txt", "r") as file:
    print(file.read())
```

---

## 5️⃣ With Statement

📄 File: `04_with.py`

### Concepts:
- Automatic file closing
- Cleaner code
- Resource management

### Example:
```python
with open("demo.txt", "r") as file:
    content = file.read()
```

---

## 6️⃣ Append Mode

📄 File: `05_append.py`

### Concepts:
- Adding data without deleting old data
- Append mode (`a`)

### Example:
```python
with open("demo.txt", "a") as file:
    file.write("Python")
```

---

## 7️⃣ Update File

📄 File: `06_update.py`

### Concepts:
- Read existing content
- Modify content
- Write updated content

### Example:
```python
updated_content = content.replace("80", "95")
```

---

## 8️⃣ Delete File

📄 File: `07_delete.py`

### Concepts:
- Delete file content
- Delete complete file
- Delete folder

### Example:
```python
os.remove("demo.txt")
```

---

## 9️⃣ Rename File

📄 File: `08_renaming.py`

### Concepts:
- Rename files
- Check file exists before renaming

### Example:
```python
os.rename("old.txt", "new.txt")
```

---

## 🔟 Create File

📄 File: `09_create.py`

### Concepts:
- Create using `w`
- Create using `a`
- Create using `x`

### Example:
```python
open("demo.txt", "w")
```

---

## 1️⃣1️⃣ Text & Binary Files

📄 File: `10_text.py`

### Text Files:
- `.txt`
- `.csv`
- `.json`
- `.xml`

### Binary Files:
- `.jpg`
- `.png`
- `.mp3`
- `.mp4`

---

## 1️⃣2️⃣ Writing Files

📄 File: `11_Write.py`

### Concepts:
- `write()`
- `writelines()`
- Difference between `w` and `a`

### Example:
```python
file.write("Hello Python")
```

---

## 1️⃣3️⃣ CSV Module

📄 File: `12.csv module.py`

### Concepts:
- CSV files
- `csv.reader`
- `csv.writer`
- `DictReader`
- `DictWriter`

### Example:
```python
import csv
```

---

## 1️⃣4️⃣ JSON Module

📄 File: `13.json module.py`

### Concepts:
- JSON basics
- `json.dumps()`
- `json.loads()`
- `json.dump()`
- `json.load()`

### Example:
```python
import json
```

---

# 🛠 Skills Learned

By completing Day 12, you learned:

✅ File handling basics  
✅ Reading files  
✅ Writing files  
✅ Updating files  
✅ Appending data  
✅ Deleting files  
✅ Renaming files  
✅ CSV handling  
✅ JSON handling  
✅ Exception handling  
✅ Text & Binary files  
✅ Real-world file operations  

---

# 💡 Real-World Applications

- Student Management System
- Banking Systems
- Log Files
- WhatsApp Backup
- CSV Dataset Handling
- API Data Storage
- Configuration Files

---

# 🚀 Mini Project Idea

## 🎓 Student Record Management System

Features:
- Add student
- View student
- Update student
- Delete student
- Export CSV
- Export JSON
- Rename backup files

---

# 📌 Technologies Used

- Python
- CSV Module
- JSON Module
- OS Module

---

# 📖 Conclusion

This day provides a complete foundation for Python File Handling.  
These concepts are highly important in:
- Backend Development
- Data Science
- Automation
- AI Projects
- Real-world Applications

---

# 👨‍💻 Author

Created while learning Python File Handling - Day 12