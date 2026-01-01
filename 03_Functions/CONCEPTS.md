# Module 3: Functions - Concepts

## 1. Function Basics

### Python vs Java

**Java:**
```java
public int add(int a, int b) {
    return a + b;
}
```

**Python:**
```python
def add(a, b):
    return a + b
```

### Key Differences:
1. Use `def` instead of type declarations
2. No return type specified (Python infers it)
3. Indentation matters (no braces)
4. No access modifiers (public, private) by default

## 2. Function Definition

```python
# Simple function with no parameters
def greet():
    print("Hello!")

greet()  # Call the function

# Function with parameters
def add(a, b):
    return a + b

result = add(5, 3)  # result = 8

# Function with multiple returns
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(10, 3)  # q=3, r=1

# Function with no return (returns None)
def print_info(name):
    print(f"Name: {name}")

print_info("Alice")  # Prints "Name: Alice"
```

## 3. Default Parameters

```python
# With default value
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()              # "Hello, Guest!"
greet("Alice")       # "Hello, Alice!"

# Multiple defaults
def create_profile(name, age=0, city="Unknown"):
    print(f"{name}, {age}, {city}")

create_profile("Bob")                    # Bob, 0, Unknown
create_profile("Bob", 30)                # Bob, 30, Unknown
create_profile("Bob", 30, "New York")    # Bob, 30, New York
```

**Important:** Default parameters must come AFTER non-default parameters!

## 4. Named Arguments (Keyword Arguments)

```python
def order_pizza(size, crust="thin", toppings="cheese"):
    print(f"Pizza: {size}, {crust}, {toppings}")

# Positional arguments
order_pizza("large")

# Named arguments
order_pizza("medium", crust="thick")
order_pizza("small", toppings="pepperoni", crust="stuffed")
order_pizza(size="large", toppings="mushroom")

# Mix positional and named (positional must come first)
order_pizza("large", toppings="pepperoni")
```

## 5. *args and **kwargs

### *args - Variable Positional Arguments

```python
# Accept any number of arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))          # 6
print(sum_all(1, 2, 3, 4, 5))    # 15

# *numbers becomes a tuple
def print_args(*args):
    for arg in args:
        print(arg)

print_args("a", "b", "c")  # Prints a, b, c
```

### **kwargs - Variable Named Arguments

```python
# Accept any number of keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# Output:
# name: Alice
# age: 30
# city: NYC

# Combining with regular parameters
def create_user(username, **details):
    print(f"User: {username}")
    for key, value in details.items():
        print(f"  {key}: {value}")

create_user("john_doe", email="john@example.com", age=25)
```

### Combined: *args and **kwargs

```python
def function(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

function(1, 2, 3, 4, 5, x=10, y=20)
# Output:
# a: 1, b: 2
# args: (3, 4, 5)
# kwargs: {'x': 10, 'y': 20}
```

## 6. Docstrings

```python
def calculate_area(length, width):
    """
    Calculate area of a rectangle.
    
    Args:
        length: Length of rectangle
        width: Width of rectangle
    
    Returns:
        Area as a float
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)
help(calculate_area)
```

## 7. Variable Scope

```python
x = 10  # Global scope

def func1():
    x = 20  # Local scope
    print(x)  # 20

func1()
print(x)  # 10 (not affected)

# To modify global variable
count = 0

def increment():
    global count  # Tell Python to use global count
    count += 1

increment()
print(count)  # 1
```

## 8. Lambda Functions

Inline functions (short and simple)

```python
# Regular function
def add(a, b):
    return a + b

# Lambda function
add = lambda a, b: a + b

# Use case: Passing function to another function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

# Sorting with lambda
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_score = sorted(students, key=lambda s: s[1])
```

## 9. Common Mistakes

```python
# ❌ Wrong: Modifying mutable default argument
def append_item(item, lst=[]):
    lst.append(item)
    return lst

append_item(1)      # [1]
append_item(2)      # [1, 2] - NOT [2]! Bug!

# ✅ Correct:
def append_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# ❌ Wrong: Using local variable before defining
def func():
    print(x)  # Error!
    x = 5

# ✅ Correct:
def func():
    x = 5
    print(x)  # 5
```

---

**Next:** Study examples.py to see real function patterns
