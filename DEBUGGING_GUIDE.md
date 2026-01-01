# Debugging Tips for Python Learners

When your code doesn't work, follow these steps!

## 1. Read the Error Message Carefully

Python error messages tell you:
- **What went wrong** (the error type)
- **Where it happened** (file name and line number)
- **Why it happened** (the message)

Example:
```
Traceback (most recent call last):
  File "program.py", line 5, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
```

This tells you:
- **Error type:** `ZeroDivisionError`
- **Location:** Line 5 in program.py
- **Cause:** Dividing by zero

## 2. Common Error Types

| Error | Cause | Fix |
|-------|-------|-----|
| `SyntaxError` | Wrong Python syntax | Check spelling, brackets, colons |
| `NameError` | Variable not defined | Define variable before using |
| `TypeError` | Wrong data type | Check variable types |
| `ValueError` | Wrong value | Check input validation |
| `IndexError` | List index too high | Check list length |
| `KeyError` | Dict key doesn't exist | Use `.get()` or check keys |
| `AttributeError` | Object doesn't have attribute | Check method/property name |
| `FileNotFoundError` | File not found | Check file path and name |
| `ZeroDivisionError` | Division by zero | Add check before division |

## 3. Debugging Techniques

### A. Print Debugging
```python
# Add print statements to track execution
def calculate(x, y):
    print(f"DEBUG: Starting with x={x}, y={y}")
    
    result = x + y
    print(f"DEBUG: After addition: {result}")
    
    result = result * 2
    print(f"DEBUG: After multiplication: {result}")
    
    return result

calculate(5, 3)
# Output shows you exactly what's happening
```

### B. Check Variable Types
```python
# Make sure variables are the right type
user_input = input("Enter age: ")
print(f"Type: {type(user_input)}")  # Will be string!

# Convert if needed
age = int(user_input)
```

### C. Use Assertions
```python
# Assert conditions you expect to be true
def calculate_percentage(part, total):
    assert total > 0, "Total must be greater than 0"
    assert part <= total, "Part cannot be greater than total"
    
    return (part / total) * 100
```

### D. Break Code Into Steps
```python
# DON'T write all in one line
result = list(map(int, input().split()))

# DO break it down
user_input = input("Enter numbers: ")
print(f"DEBUG: user_input = {user_input}")

numbers = user_input.split()
print(f"DEBUG: after split = {numbers}")

result = list(map(int, numbers))
print(f"DEBUG: after conversion = {result}")
```

### E. Test With Simple Data
```python
# Instead of using real data, start with simple cases
lst = [1, 2, 3]  # Simple list
# vs
lst = [random data from file]  # Harder to debug

# Test with the simple case first, then add complexity
```

## 4. Off-by-One Errors

Common in loops and lists:

```python
# WRONG: Misses last element (list is 0-indexed)
for i in range(len(lst)):  # Oops, this is right!
    print(lst[i])

# RIGHT: Use direct iteration
for item in lst:
    print(item)

# WRONG: Wrong slice end
lst[0:3]  # Gets items 0,1,2 (not 3)

# RIGHT: If you want first 3
lst[0:3] or lst[:3]
```

## 5. Type Mismatch Errors

```python
# WRONG: Mixing types
x = "5"
y = 10
z = x + y  # ERROR! Can't add string and int

# RIGHT: Convert types
x = int("5")  # Convert string to int
z = x + y  # 15

# Also watch for:
lst = [1, 2, 3]
result = sum(lst)  # Works

lst = ["a", "b", "c"]
result = sum(lst)  # ERROR! Can't sum strings
```

## 6. Scope Issues

```python
# WRONG: Using variable outside its scope
try:
    x = 10
except:
    pass

print(x)  # This works if except block doesn't execute
# But what if it does? x might not exist!

# RIGHT: Define outside the try block
x = None
try:
    x = 10
except:
    x = 0

print(x)  # Always defined
```

## 7. Mutable Default Arguments (Tricky!)

```python
# WRONG: Mutable default argument
def append_item(item, lst=[]):
    lst.append(item)
    return lst

append_item(1)  # [1]
append_item(2)  # [1, 2] <- Problem! List is shared!

# RIGHT: Use None as default
def append_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

append_item(1)  # [1]
append_item(2)  # [2] <- Better
```

## 8. String vs Integer

```python
# These are NOT the same:
x = "42"   # String
y = 42     # Integer

print(x == y)  # False!
print(x + 8)   # ERROR! Can't add string and int
print(y + 8)   # 50 works fine

# Always convert user input:
age = int(input("Enter age: "))  # Convert to int
```

## 9. Using the Python Debugger (pdb)

```python
# Add breakpoint in your code
def calculate(x, y):
    import pdb; pdb.set_trace()  # Execution pauses here
    
    result = x + y
    return result

# Commands in debugger:
# n = next line
# s = step into function
# c = continue
# p variable = print variable
# l = list code
# q = quit
```

## 10. Checklist When Code Doesn't Work

- [ ] Read the error message carefully
- [ ] Check for typos in variable names
- [ ] Check for correct data types
- [ ] Verify all variables are defined
- [ ] Check loop conditions
- [ ] Verify list/dict keys exist
- [ ] Test with simple data first
- [ ] Add print statements
- [ ] Check file paths for file operations
- [ ] Handle edge cases (empty lists, None values, etc.)

## 11. Java Developer Tips

Since you know Java, remember:

| Java | Python | Common Mistake |
|------|--------|---|
| `new ArrayList()` | `[]` | Forgetting list is mutable |
| `null` | `None` | Using `None` in comparisons |
| `arr.length` | `len(arr)` | Using `length` method that doesn't exist |
| Type declarations | Dynamic typing | Not converting types when needed |
| `for (int i=0; i<10; i++)` | `for i in range(10)` | Using C-style loop |
| `public class X` | `class X` | Over-using OOP in Python |

## 12. Helpful Python Commands

```python
# Get information about object
help(str.split)           # Help on method
dir(string_var)          # Available methods/attributes
type(variable)           # Get type
isinstance(x, int)       # Check type
len(something)           # Length
id(object)              # Object memory address

# Introspection
import inspect
inspect.getsource(function)  # Get function source code
```

---

**Remember:** Debugging is a skill! The more you practice, the faster you'll find and fix errors. Be patient with yourself! 🐛
