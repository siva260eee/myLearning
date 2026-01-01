# Quick Reference Guide

Use this when you need to quickly look up Python syntax!

## Variables and Types
```python
x = 5                           # int
name = "Alice"                  # string
height = 5.8                    # float
is_student = True              # boolean
nothing = None                 # null value
```

## Operators
```python
a + b, a - b, a * b, a / b     # Arithmetic
a // b, a % b, a ** b          # Floor div, modulo, exponent
a == b, a != b                 # Comparison
a < b, a > b, a <= b, a >= b   # Comparison
a and b, a or b, not a         # Logical
```

## Strings
```python
name = "Alice"
name[0]                        # 'A' (index)
name[1:3]                      # 'li' (slice)
name[::-1]                     # 'ecilA' (reverse)
len(name)                      # 5
name.upper(), name.lower()     # Uppercase, lowercase
name.replace("A", "B")         # Replace
name.split(",")                # Split
",".join(["a", "b"])          # Join
f"Name: {name}"               # f-string
```

## Lists
```python
lst = [1, 2, 3, 4, 5]
lst[0]                         # 1 (first)
lst[-1]                        # 5 (last)
lst[1:3]                       # [2, 3] (slice)
lst.append(6)                  # Add to end
lst.remove(2)                  # Remove by value
lst.pop()                      # Remove and return last
lst.sort()                     # Sort
len(lst)                       # Length
sum(lst), max(lst), min(lst)   # Statistics
[x**2 for x in lst]            # List comprehension
```

## Tuples
```python
pt = (10, 20)
pt[0]                          # 10
x, y = pt                      # Unpacking
(1, 2, 3)[0:2]                # (1, 2) slicing works
# Tuples are immutable - can't change!
```

## Sets
```python
s = {1, 2, 3, 3}               # {1, 2, 3} (no duplicates)
s.add(4)                       # Add element
s.remove(2)                    # Remove element
s1 | s2                        # Union
s1 & s2                        # Intersection
s1 - s2                        # Difference
1 in s                         # Membership test
```

## Dictionaries
```python
d = {"name": "Alice", "age": 30}
d["name"]                      # "Alice"
d.get("age", 0)               # 30 (default if not found)
d["job"] = "Engineer"         # Add/update
del d["name"]                  # Delete
d.keys(), d.values(), d.items() # Keys, values, items
for k, v in d.items():        # Iterate
```

## Control Flow
```python
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

while x > 0:
    print(x)
    x -= 1

for i in range(5):            # 0 to 4
    print(i)

for item in lst:
    print(item)

for i, item in enumerate(lst): # With index
    print(i, item)

if x in lst:                   # Membership
    print("found")
```

## Functions
```python
def greet(name="Guest"):
    return f"Hello, {name}!"

def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

lambda x: x**2                 # Lambda function
sorted(lst, key=lambda x: x)   # Sort with key
```

## Classes
```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hi, {self.name}"

p = Person("Alice")
p.greet()

class Student(Person):         # Inheritance
    def study(self):
        return "Studying"

s = Student("Bob")
```

## Error Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error!")
except Exception as e:
    print(f"Unexpected: {e}")
else:
    print("Success!")
finally:
    print("Cleanup")

# Raise exception
raise ValueError("Invalid value")
```

## File I/O
```python
# Read
with open("file.txt", "r") as f:
    content = f.read()
    lines = f.readlines()

# Write
with open("file.txt", "w") as f:
    f.write("content")

# JSON
import json
json.dump(data, f)            # Save
data = json.load(f)           # Load

# CSV
import csv
reader = csv.reader(f)
writer = csv.writer(f)
```

## Useful Functions
```python
len(obj)                       # Length
max(lst), min(lst)            # Max/min
sum(lst)                      # Sum
sorted(lst)                   # Sorted copy
list(range(5))                # [0,1,2,3,4]
enumerate(lst)                # With indices
zip(lst1, lst2)               # Pair elements
map(func, lst)                # Apply function
filter(func, lst)             # Filter elements
all([True, True])             # All true?
any([False, True])            # Any true?
```

## Common Patterns
```python
# Count occurrences
counter = {}
for item in lst:
    counter[item] = counter.get(item, 0) + 1

# Find duplicates
seen = set()
duplicates = []
for item in lst:
    if item in seen:
        duplicates.append(item)
    seen.add(item)

# Swap variables
a, b = b, a

# Default values
value = obj.get("key", "default")

# Check multiple conditions
if a < x < b:  # Chained comparison
    print("x is between a and b")
```

## Debugging
```python
print(f"Debug: {variable}")    # Print statements
assert condition, "message"    # Assertions
import pdb; pdb.set_trace()   # Debugger (breakpoint)
type(obj)                      # Get type
dir(obj)                       # List attributes
help(function)                 # Get help
```

## Import Statements
```python
import os                      # Import module
from os import path           # Import specific
from os import path as p      # Import with alias
import os as o                # Module alias
from os import *              # Import all (avoid!)

# Standard library
import json, csv, os, sys
import datetime, time
import random, math
import collections, itertools
```

---

Keep this guide handy while you code! 📖
