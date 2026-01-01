# Module 2: Control Flow - Concepts

## 1. if/elif/else Statements

### Python vs Java

**Java:**
```java
if (age >= 18) {
    System.out.println("Adult");
} else if (age >= 13) {
    System.out.println("Teen");
} else {
    System.out.println("Child");
}
```

**Python:**
```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

### Key Differences:
1. Use `:` after condition
2. Use **indentation** (not braces `{}`)
3. `elif` instead of `else if`
4. No parentheses needed around condition

### Truthiness in Python
Any value can be evaluated as True or False:
- **False:** `False`, `0`, `0.0`, `""`, `[]`, `{}`, `None`
- **True:** Everything else (`True`, non-zero numbers, non-empty strings/lists)

```python
if name:  # True if name is not empty string
    print("Name exists")

if items:  # True if items list is not empty
    print("Have items")
```

## 2. for Loops

### Iterating with range()

```python
# 0 to 4 (5 not included)
for i in range(5):
    print(i)  # Prints: 0, 1, 2, 3, 4

# 2 to 5 (start, end)
for i in range(2, 6):
    print(i)  # Prints: 2, 3, 4, 5

# 0 to 10 step by 2
for i in range(0, 11, 2):
    print(i)  # Prints: 0, 2, 4, 6, 8, 10

# Reverse
for i in range(5, 0, -1):
    print(i)  # Prints: 5, 4, 3, 2, 1
```

### Iterating over Collections

```python
fruits = ["apple", "banana", "cherry"]

# Direct iteration
for fruit in fruits:
    print(fruit)

# With index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# String iteration
for char in "Python":
    print(char)  # Prints each character
```

### Comparison: Java vs Python

**Java:**
```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

for (String fruit : fruits) {
    System.out.println(fruit);
}
```

**Python:**
```python
for i in range(5):
    print(i)

for fruit in fruits:
    print(fruit)
```

## 3. while Loops

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# With condition
password = ""
while password != "secret":
    password = input("Enter password: ")
    if password == "secret":
        print("Access granted")
    else:
        print("Try again")
```

### Loop Control

```python
# break - exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints: 0, 1, 2, 3, 4

# continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints: 0, 1, 3, 4

# else on loops (runs if loop completes normally)
for i in range(3):
    print(i)
else:
    print("Loop completed")  # Prints this
    
for i in range(5):
    if i == 2:
        break
else:
    print("Loop completed")  # Does NOT print (due to break)
```

## 4. Nested Loops

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}*{j}={i*j}", end=" ")
    print()  # Newline
```

**Output:**
```
1*1=1 1*2=2 1*3=3 
2*1=2 2*2=4 2*3=6 
3*1=3 3*2=6 3*3=9 
```

## 5. Important Python Idioms

### No need for C-style loops
```python
# DON'T do this (Java style)
i = 0
while i < len(items):
    print(items[i])
    i += 1

# DO this (Pythonic)
for item in items:
    print(item)

# If you need index
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

### List Comprehension (Advanced)
```python
# Traditional way
squares = []
for i in range(5):
    squares.append(i ** 2)

# Pythonic way (list comprehension)
squares = [i ** 2 for i in range(5)]  # [0, 1, 4, 9, 16]

# With condition
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]  # [0, 4, 16, 36, 64]
```

---

**Next:** Study examples.py to see real-world patterns
