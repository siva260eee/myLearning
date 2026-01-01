# Module 2: Control Flow - Examples

print("=" * 50)
print("1. IF/ELIF/ELSE STATEMENTS")
print("=" * 50)

# Simple if
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade F")

# Truthiness
name = "Alice"
if name:  # True because non-empty string
    print(f"Hello, {name}!")

items = []
if items:
    print("Items exist")
else:
    print("No items")

print("\n" + "=" * 50)
print("2. FOR LOOPS WITH range()")
print("=" * 50)

# Basic for loop
print("Loop from 0 to 4:")
for i in range(5):
    print(i, end=" ")
print()

# With start and stop
print("\nLoop from 2 to 5:")
for i in range(2, 6):
    print(i, end=" ")
print()

# With step
print("\nEven numbers 0-10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# Reverse
print("\nCountdown from 5 to 1:")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

print("\n" + "=" * 50)
print("3. FOR LOOPS OVER COLLECTIONS")
print("=" * 50)

fruits = ["apple", "banana", "cherry", "date"]

# Simple iteration
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# With enumerate (get index and value)
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# String iteration
print("\nCharacters in 'Python':")
for char in "Python":
    print(char, end=" ")
print()

print("\n" + "=" * 50)
print("4. WHILE LOOPS")
print("=" * 50)

# Countdown
print("Countdown from 3:")
count = 3
while count > 0:
    print(count)
    count -= 1
print("Blastoff!")

# Loop with condition
print("\nFinding a number (0-5):")
import random
secret = random.randint(0, 5)
guess = -1
attempts = 0
while guess != secret:
    guess = int(input("Guess a number (0-5): "))
    attempts += 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! ({attempts} attempts)")

print("\n" + "=" * 50)
print("5. BREAK AND CONTINUE")
print("=" * 50)

# Break - exit the loop
print("Numbers until we hit 5:")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print("\n(stopped at 5)")

# Continue - skip to next
print("\nNumbers except 3:")
for i in range(6):
    if i == 3:
        continue
    print(i, end=" ")
print()

# Find first number divisible by 7 in range
print("\nFinding first number > 10 divisible by 7:")
for num in range(11, 50):
    if num % 7 == 0:
        print(f"Found: {num}")
        break

print("\n" + "=" * 50)
print("6. FOR-ELSE (unique to Python)")
print("=" * 50)

# Else runs if loop completes normally (no break)
print("Searching for 3 in list:")
numbers = [1, 2, 4, 5]
for num in numbers:
    if num == 3:
        print("Found 3!")
        break
else:
    print("3 not found")  # This prints

print("\nSearching for 2 in list:")
for num in numbers:
    if num == 2:
        print("Found 2!")
        break
else:
    print("2 not found")  # This does NOT print

print("\n" + "=" * 50)
print("7. NESTED LOOPS")
print("=" * 50)

# Simple multiplication table
print("3x3 Multiplication Table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j:2}", end=" ")  # :2 means width of 2
    print()

# Nested loops with break
print("\nFinding pairs that sum to 7:")
for i in range(1, 4):
    for j in range(1, 4):
        if i + j == 7:
            print(f"{i} + {j} = 7")
            break

print("\n" + "=" * 50)
print("8. LIST COMPREHENSION")
print("=" * 50)

# Traditional way
squares = []
for i in range(5):
    squares.append(i ** 2)
print(f"Squares (traditional): {squares}")

# Pythonic way (list comprehension)
squares = [i ** 2 for i in range(5)]
print(f"Squares (comprehension): {squares}")

# With condition
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(f"Even squares: {even_squares}")

# Transform strings
words = ["python", "java", "javascript"]
uppercase = [word.upper() for word in words]
print(f"Uppercase: {uppercase}")

print("\n" + "=" * 50)
print("9. PRACTICAL EXAMPLE: GRADE COUNTER")
print("=" * 50)

# Count grades
grades = [85, 92, 78, 95, 88, 91, 72, 98]

print(f"All grades: {grades}")

count_a = 0
count_b = 0
count_c = 0
count_f = 0

for grade in grades:
    if grade >= 90:
        count_a += 1
    elif grade >= 80:
        count_b += 1
    elif grade >= 70:
        count_c += 1
    else:
        count_f += 1

print(f"A's: {count_a}")
print(f"B's: {count_b}")
print(f"C's: {count_c}")
print(f"F's: {count_f}")
print(f"Average: {sum(grades) / len(grades):.2f}")

print("\n" + "=" * 50)
print("END OF EXAMPLES")
print("=" * 50)
