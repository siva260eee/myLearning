# Module 5: Data Structures - Examples

print("=" * 60)
print("1. LISTS - CREATION AND OPERATIONS")
print("=" * 60)

# Create lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True, None]

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Length: {len(fruits)}")

# Access elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second and third: {fruits[1:3]}")

# Modify lists
fruits.append("date")
print(f"After append: {fruits}")

fruits.insert(1, "blueberry")
print(f"After insert: {fruits}")

removed = fruits.pop()
print(f"Removed: {removed}, List: {fruits}")

fruits.remove("blueberry")
print(f"After remove: {fruits}")

# List methods
numbers = [3, 1, 4, 1, 5]
print(f"\nOriginal: {numbers}")
print(f"Sorted: {sorted(numbers)}")
print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 5: {numbers.index(5)}")

print("\n" + "=" * 60)
print("2. LIST SLICING")
print("=" * 60)

items = ["a", "b", "c", "d", "e"]
print(f"Items: {items}")
print(f"[0:2]: {items[0:2]}")
print(f"[1:4]: {items[1:4]}")
print(f"[:3]: {items[:3]}")
print(f"[2:]: {items[2:]}")
print(f"[::2] (every 2): {items[::2]}")
print(f"[::-1] (reversed): {items[::-1]}")

print("\n" + "=" * 60)
print("3. LIST COMPREHENSION")
print("=" * 60)

# Generate list of squares
squares = [x**2 for x in range(6)]
print(f"Squares: {squares}")

# Filter even numbers
numbers = range(10)
evens = [n for n in numbers if n % 2 == 0]
print(f"Evens: {evens}")

# Transform strings
words = ["hello", "world", "python"]
uppercase = [w.upper() for w in words]
print(f"Uppercase: {uppercase}")

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"3x3 Matrix: {matrix}")

print("\n" + "=" * 60)
print("4. TUPLES")
print("=" * 60)

# Create tuple
point = (10, 20)
colors = ("red", "green", "blue")
single = (42,)  # Important: comma!

print(f"Point: {point}")
print(f"Colors: {colors}")
print(f"Length: {len(colors)}")

# Access
print(f"First color: {colors[0]}")
print(f"Slice: {colors[0:2]}")

# Unpacking
x, y = point
r, g, b = colors
print(f"Unpacked point: x={x}, y={y}")
print(f"Unpacked colors: r={r}, g={g}, b={b}")

# Tuple methods
print(f"Index of 'green': {colors.index('green')}")
print(f"Count of 'red': {colors.count('red')}")

# Can't modify
try:
    colors[0] = "yellow"
except TypeError as e:
    print(f"Error: {e}")

# But can create new tuple
colors = colors + ("yellow",)
print(f"New colors: {colors}")

print("\n" + "=" * 60)
print("5. SETS")
print("=" * 60)

# Create sets
numbers = {1, 2, 3, 3, 2}  # Duplicates removed
print(f"Numbers: {numbers}")

colors = {"red", "green", "blue"}
print(f"Colors: {colors}")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(f"\nSet1: {set1}")
print(f"Set2: {set2}")
print(f"Union (|): {set1 | set2}")
print(f"Intersection (&): {set1 & set2}")
print(f"Difference (-): {set1 - set2}")

# Set methods
colors.add("yellow")
print(f"After add: {colors}")

colors.remove("red")
print(f"After remove: {colors}")

# Membership test
if "green" in colors:
    print("Green found!")

print("\n" + "=" * 60)
print("6. DICTIONARIES")
print("=" * 60)

# Create dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "NYC",
    "job": "Engineer"
}

print(f"Person: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Country: {person.get('country', 'USA')}")  # Default value

# Modify
person["age"] = 31
person["email"] = "alice@example.com"
del person["city"]
print(f"\nModified: {person}")

# Iteration
print("\nIterating over items:")
for key, value in person.items():
    print(f"  {key}: {value}")

print("\nIterating over keys:")
for key in person:
    print(f"  {key}")

# Check key exists
if "email" in person:
    print(f"Email exists: {person['email']}")

print("\n" + "=" * 60)
print("7. DICTIONARY OPERATIONS")
print("=" * 60)

scores = {"alice": 95, "bob": 87, "charlie": 92}
print(f"Scores: {scores}")
print(f"Keys: {list(scores.keys())}")
print(f"Values: {list(scores.values())}")
print(f"Items: {list(scores.items())}")

# Merge dictionaries
student1 = {"name": "Alice", "age": 20}
student1.update({"gpa": 3.8, "major": "CS"})
print(f"Updated: {student1}")

# Create from list
keys = ["a", "b", "c"]
values = [1, 2, 3]
paired = dict(zip(keys, values))
print(f"Paired: {paired}")

print("\n" + "=" * 60)
print("8. DICTIONARY COMPREHENSION")
print("=" * 60)

# Create dictionary
numbers = range(6)
squares_dict = {n: n**2 for n in numbers}
print(f"Squares: {squares_dict}")

# With condition
evens_dict = {n: n**2 for n in range(10) if n % 2 == 0}
print(f"Evens squared: {evens_dict}")

# Transform existing dict
person = {"alice": 25, "bob": 30, "charlie": 22}
older = {name: age for name, age in person.items() if age >= 25}
print(f"People >= 25: {older}")

print("\n" + "=" * 60)
print("9. SORTING")
print("=" * 60)

# Sort list
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")
print(f"Sorted: {sorted(numbers)}")
print(f"Reverse: {sorted(numbers, reverse=True)}")

# Sort strings
words = ["python", "java", "c", "javascript"]
print(f"Words: {words}")
print(f"Sorted: {sorted(words)}")
print(f"By length: {sorted(words, key=len)}")

# Sort list of tuples
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
print(f"\nStudents: {students}")
print(f"By name: {sorted(students, key=lambda s: s[0])}")
print(f"By score: {sorted(students, key=lambda s: s[1])}")

print("\n" + "=" * 60)
print("10. PRACTICAL EXAMPLE: STUDENT GRADES")
print("=" * 60)

grades = {
    "Alice": [85, 92, 88],
    "Bob": [78, 81, 76],
    "Charlie": [95, 98, 92]
}

# Calculate averages
for name, scores in grades.items():
    avg = sum(scores) / len(scores)
    print(f"{name}: {scores} → Average: {avg:.2f}")

# Find top student
top_student = max(grades.items(), key=lambda item: sum(item[1])/len(item[1]))
print(f"\nTop student: {top_student[0]}")

print("\n" + "=" * 60)
print("END OF EXAMPLES")
print("=" * 60)
