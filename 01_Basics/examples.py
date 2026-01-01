# Module 1: Basics - Examples
# Read through these examples and understand each concept

print("=" * 50)
print("1. VARIABLES AND DATA TYPES")
print("=" * 50)

# Variables - no type declaration needed
age = 25
name = "Alice"
height = 5.8
is_student = True
nothing = None

print(f"Age: {age}, Type: {type(age)}")
print(f"Name: {name}, Type: {type(name)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")
print(f"Nothing: {nothing}, Type: {type(nothing)}")

# Dynamic typing - reassign to different type
value = 42
print(f"\nBefore: value = {value}, type = {type(value)}")
value = "Now I'm a string"
print(f"After: value = {value}, type = {type(value)}")

print("\n" + "=" * 50)
print("2. ARITHMETIC OPERATORS")
print("=" * 50)

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")  # Returns float
print(f"Floor Division: {a} // {b} = {a // b}")  # Returns int
print(f"Modulo: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

print("\n" + "=" * 50)
print("3. COMPARISON OPERATORS")
print("=" * 50)

x = 5
y = 10

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x < y: {x < y}")
print(f"x > y: {x > y}")
print(f"x <= y: {x <= y}")
print(f"x >= y: {x >= y}")

print("\n" + "=" * 50)
print("4. LOGICAL OPERATORS")
print("=" * 50)

p = True
q = False

print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not p: {not p}")
print(f"not q: {not q}")

# Real-world example
age = 25
income = 50000
can_loan = age >= 21 and income >= 30000
print(f"\nCan get loan (age>=21 AND income>=30000): {can_loan}")

print("\n" + "=" * 50)
print("5. STRING OPERATIONS")
print("=" * 50)

text = "Python"
sentence = "Hello World Python"

print(f"Text: {text}")
print(f"Length: {len(text)}")
print(f"First character [0]: {text[0]}")
print(f"Last character [-1]: {text[-1]}")
print(f"Substring [1:4] (index 1 to 3): {text[1:4]}")
print(f"Every other character [::2]: {text[::2]}")
print(f"Reversed [::-1]: {text[::-1]}")

print(f"\nSentence: {sentence}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Replace 'World' with 'Everyone': {sentence.replace('World', 'Everyone')}")
print(f"Split by space: {sentence.split(' ')}")
print(f"Count 'o': {sentence.count('o')}")
print(f"Starts with 'Hello': {sentence.startswith('Hello')}")
print(f"Ends with 'Python': {sentence.endswith('Python')}")

print("\n" + "=" * 50)
print("6. TYPE CASTING")
print("=" * 50)

# String to number
str_number = "42"
str_decimal = "3.14"

num_int = int(str_number)
num_float = float(str_decimal)

print(f"String '{str_number}' as int: {num_int}, type: {type(num_int)}")
print(f"String '{str_decimal}' as float: {num_float}, type: {type(num_float)}")

# Number to string
num = 100
num_as_string = str(num)
print(f"Number {num} as string: '{num_as_string}', type: {type(num_as_string)}")

# To boolean (0 is False, non-zero is True)
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")  # Empty string is False
print(f"bool('hello'): {bool('hello')}")  # Non-empty string is True
print(f"bool([]): {bool([])}")  # Empty list is False
print(f"bool([1,2]): {bool([1, 2])}")  # Non-empty list is True

print("\n" + "=" * 50)
print("7. F-STRINGS (String Formatting)")
print("=" * 50)

name = "Bob"
age = 30
score = 95.5

# f-strings are powerful
print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My score is {score:.1f}")  # .1f means 1 decimal place
print(f"My score is {score:.0f}")  # .0f means no decimal places
print(f"Formatted: Name={name:>10}, Age={age:02d}")  # Right align, zero padding

print("\n" + "=" * 50)
print("8. INPUT/OUTPUT")
print("=" * 50)

# Uncomment the lines below to test input
# user_name = input("What is your name? ")
# print(f"Hello, {user_name}!")
#
# user_age = int(input("How old are you? "))
# print(f"You are {user_age} years old")

print("(Commented out - uncomment to test interactive input)")

print("\n" + "=" * 50)
print("9. VARIABLE NAMING AND CONVENTIONS")
print("=" * 50)

# Python uses snake_case (not camelCase like Java)
first_name = "John"
last_name = "Doe"
email_address = "john@example.com"
is_active = True

# These are discouraged
firstName = "John"  # camelCase - avoid in Python
FirstName = "John"  # PascalCase - use for classes only

print(f"Convention - snake_case: {first_name} {last_name}")
print(f"Email: {email_address}")
print(f"Active: {is_active}")

print("\n" + "=" * 50)
print("END OF EXAMPLES")
print("=" * 50)
