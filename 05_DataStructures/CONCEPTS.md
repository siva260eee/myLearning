# Module 5: Data Structures - Concepts

## 1. Lists

Python lists are like Java's `ArrayList`.

### Creating Lists
```python
# Empty list
items = []

# With values
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # Can mix types

# Using constructor
my_list = list()  # Empty list
my_list = list("abc")  # ['a', 'b', 'c']
```

### Accessing Elements
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # "apple" (0-indexed)
print(fruits[-1])     # "cherry" (last element)
print(fruits[1:3])    # ["banana", "cherry"] (slice, end excluded)
print(fruits[:2])     # ["apple", "banana"]
print(fruits[1:])     # ["banana", "cherry"]
```

### List Methods
```python
fruits = ["apple", "banana"]

fruits.append("cherry")           # Add to end
fruits.insert(1, "blueberry")     # Insert at index
removed = fruits.pop()            # Remove and return last
removed = fruits.pop(0)           # Remove and return at index
fruits.remove("banana")           # Remove by value
fruits.clear()                    # Remove all
fruits.extend([1, 2, 3])          # Add multiple
index = fruits.index("apple")     # Find index of value
count = fruits.count("apple")     # Count occurrences
fruits.sort()                     # Sort in place
fruits.reverse()                  # Reverse in place
copy = fruits.copy()              # Shallow copy
```

### List Comprehension
```python
# Traditional
squares = []
for i in range(5):
    squares.append(i ** 2)

# Comprehension (more Pythonic)
squares = [i ** 2 for i in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [i for i in range(10) if i % 2 == 0]  # [0, 2, 4, 6, 8]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
```

## 2. Tuples

Immutable lists (can't change after creation).

```python
# Create tuple
coordinates = (10, 20)
colors = ("red", "green", "blue")
single = (42,)  # Comma needed!

# Access like list
print(coordinates[0])    # 10
print(colors[1:3])       # ("green", "blue")

# Unpacking
x, y = coordinates
r, g, b = colors

# Methods
print(colors.count("red"))    # 1
print(colors.index("blue"))   # 2

# Can't modify
# colors[0] = "yellow"  # ERROR!
```

## 3. Sets

Unordered collection of unique values (like Java's `HashSet`).

```python
# Create set
numbers = {1, 2, 3, 3, 2}  # {1, 2, 3} - duplicates removed
unique = set([1, 1, 2, 2, 3])  # {1, 2, 3}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection: {3}
print(set1 - set2)  # Difference: {1, 2}

# Methods
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.remove("red")
colors.discard("yellow")  # No error if not found
colors.clear()

# Membership test (fast)
if "red" in colors:
    print("Red found")
```

## 4. Dictionaries

Key-value pairs (like Java's `HashMap`).

```python
# Create dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "NYC"
}

# Alternate syntax
scores = dict(alice=95, bob=87, charlie=92)

# Access
print(person["name"])         # "Alice"
print(person.get("age"))      # 30
print(person.get("job", "N/A"))  # "N/A" (default if not found)

# Modify
person["age"] = 31
person["job"] = "Engineer"
del person["city"]

# Methods
print(person.keys())          # dict_keys(['name', 'age', 'job'])
print(person.values())        # dict_values(['Alice', 31, 'Engineer'])
print(person.items())         # Key-value pairs

# Iteration
for key, value in person.items():
    print(f"{key}: {value}")

for key in person:
    print(f"{key}: {person[key]}")

# Merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3}
merged = {**dict1, **dict2}  # {"a": 1, "b": 2, "c": 3}

# Check key existence
if "name" in person:
    print(person["name"])
```

### Dictionary Comprehension
```python
# Create dict from list
numbers = [1, 2, 3, 4, 5]
squares = {n: n**2 for n in numbers}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
evens = {n: n**2 for n in numbers if n % 2 == 0}  # {2: 4, 4: 16}
```

## 5. Choosing the Right Data Structure

| Structure | Purpose | Mutable | Ordered | Unique |
|-----------|---------|---------|---------|--------|
| List | Flexible collection | Yes | Yes | No |
| Tuple | Fixed collection | No | Yes | No |
| Set | Unique values | Yes | No | Yes |
| Dict | Key-value pairs | Yes | No (keys unique) | - |

- **List:** When you need an ordered collection that changes
- **Tuple:** When you need immutable data (dictionary keys, return multiple values)
- **Set:** When you need unique values and fast membership test
- **Dict:** When you need fast lookups by key

## 6. Sorting

```python
# Sort lists
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers_sorted = sorted(numbers)  # Returns new list [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort()  # Sorts in place

# Reverse sort
sorted(numbers, reverse=True)

# Sort by key
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
by_score = sorted(students, key=lambda s: s[1])
by_name = sorted(students, key=lambda s: s[0])

# Custom objects
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("Alice", 85), Student("Bob", 92)]
by_score = sorted(students, key=lambda s: s.score)
```

---

**Next:** Study examples.py to see practical patterns
