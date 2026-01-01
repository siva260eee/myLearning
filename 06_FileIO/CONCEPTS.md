# Module 6: File I/O - Concepts

## 1. Reading and Writing Files

### Opening Files

```python
# Basic open - must close manually
f = open("file.txt", "r")
# ... do something
f.close()

# Better way - automatic closing (context manager)
with open("file.txt", "r") as f:
    # ... do something
# File automatically closed

# File modes:
# "r" - Read (default)
# "w" - Write (creates/overwrites)
# "a" - Append (add to end)
# "x" - Create (error if exists)
# "b" - Binary mode (e.g., "rb", "wb")
```

### Reading File Content

```python
with open("data.txt", "r") as f:
    # Method 1: Read all as string
    content = f.read()
    
    # Method 2: Read all as list of lines
    lines = f.readlines()  # Includes '\n'
    
    # Method 3: Read one line
    line = f.readline()
    
    # Method 4: Iterate through lines (efficient)
    for line in f:
        print(line.strip())  # .strip() removes '\n'
```

### Writing to Files

```python
# Write (overwrites entire file)
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")

# Append to file
with open("output.txt", "a") as f:
    f.write("Appended line\n")

# Write multiple lines
with open("output.txt", "w") as f:
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    f.writelines(lines)
```

## 2. Working with Text Files

### Basic File Operations

```python
# Count lines in file
with open("data.txt", "r") as f:
    line_count = sum(1 for line in f)

# Copy file
with open("original.txt", "r") as f_in:
    content = f_in.read()

with open("copy.txt", "w") as f_out:
    f_out.write(content)

# Read and modify
with open("data.txt", "r") as f:
    lines = f.readlines()

with open("data.txt", "w") as f:
    for line in lines:
        f.write(line.upper())  # Write uppercase
```

### File Path Handling

```python
import os

# Check if file exists
if os.path.exists("file.txt"):
    print("File exists")

# Check if it's a file
if os.path.isfile("file.txt"):
    print("It's a file")

# Get file size
size = os.path.getsize("file.txt")

# Get directory
dirname = os.path.dirname("folder/file.txt")

# Get filename
basename = os.path.basename("folder/file.txt")

# Join paths (better than string concatenation)
path = os.path.join("folder", "subfolder", "file.txt")

# List files in directory
files = os.listdir("folder")

# Get absolute path
abs_path = os.path.abspath("file.txt")
```

## 3. Working with JSON

JSON is like serializing objects to text.

```python
import json

# Dictionary to JSON
data = {"name": "Alice", "age": 30, "hobbies": ["reading", "coding"]}
json_string = json.dumps(data)  # Returns string
# '{"name": "Alice", "age": 30, "hobbies": ["reading", "coding"]}'

# JSON to Dictionary
parsed = json.loads(json_string)  # Returns dict

# Write JSON to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)  # indent for readability

# Read JSON from file
with open("data.json", "r") as f:
    data = json.load(f)  # Returns dict
```

## 4. Working with CSV

CSV = Comma-Separated Values

```python
import csv

# Write CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "NYC"],
    ["Bob", 25, "LA"],
    ["Charlie", 35, "Chicago"]
]

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read CSV - as list of lists
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ['Name', 'Age', 'City']

# Read CSV - as dictionaries (DictReader)
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # {'Name': 'Alice', 'Age': '30', 'City': 'NYC'}

# Write CSV with dictionaries
data = [
    {"Name": "Alice", "Age": 30, "City": "NYC"},
    {"Name": "Bob", "Age": 25, "City": "LA"}
]

with open("data.csv", "w", newline="") as f:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```

## 5. Error Handling for Files

```python
import os

# Check before opening
if os.path.exists("file.txt"):
    with open("file.txt", "r") as f:
        content = f.read()

# Try/except for errors
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except IOError as e:
    print(f"Error reading file: {e}")

# Check if readable/writable
try:
    f = open("file.txt", "r")
    if f.readable():
        content = f.read()
    f.close()
except PermissionError:
    print("Don't have permission!")
```

## 6. Working with Directories

```python
import os
import shutil

# Create directory
os.makedirs("new_folder")

# Create nested directories
os.makedirs("folder/subfolder/nested", exist_ok=True)

# Remove directory
os.rmdir("empty_folder")  # Only if empty
shutil.rmtree("folder")   # Remove with contents

# List directories
dirs = [d for d in os.listdir(".") if os.path.isdir(d)]

# Walk through directories
for root, dirs, files in os.walk("."):
    print(f"Directory: {root}")
    print(f"Files: {files}")
```

---

**Next:** Study examples.py for practical file operations
