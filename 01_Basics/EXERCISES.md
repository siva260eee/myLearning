# Module 1: Basics - Exercises

Complete these exercises in a file called `my_solutions.py`. Write the code yourself!

## Exercise 1: Variables and Output
Create variables for:
- Your name (string)
- Your age (integer)
- Your height in meters (float)
- Whether you code (boolean)

Print all of them using f-strings.

**Expected Output Example:**
```
My name is Alice
I am 25 years old
My height is 1.75 meters
I code: True
```

---

## Exercise 2: Arithmetic Operations
Write a program that:
1. Takes two numbers from the user
2. Calculates and prints: sum, difference, product, division, floor division, and modulo

**Expected Output Example (for inputs 10 and 3):**
```
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.333...
10 // 3 = 3
10 % 3 = 1
```

---

## Exercise 3: String Operations
Given the string: `"Python Programming"`

1. Print the length
2. Print the first 3 characters
3. Print the last 5 characters
4. Print it in uppercase
5. Print it in lowercase
6. Replace "Python" with "Java"
7. Check if it contains "Program"

**Your code should work for ANY string (make it a variable)**

---

## Exercise 4: Temperature Converter
Write a program that:
1. Takes temperature in Celsius from user
2. Converts to Fahrenheit using formula: F = (C × 9/5) + 32
3. Prints the result with 2 decimal places

**Expected Output (for input 25):**
```
25°C = 77.00°F
```

---

## Exercise 5: Age Category
Write a program that:
1. Takes age as input
2. Uses comparison operators to determine:
   - "Child" if age < 13
   - "Teen" if 13 <= age < 18
   - "Adult" if 18 <= age < 65
   - "Senior" if age >= 65

**Expected Output (for input 25):**
```
You are an Adult
```

---

## Exercise 6: Boolean Logic
Create variables for:
- `has_license` (boolean)
- `has_insurance` (boolean)

Print whether a person can drive using logical operators:
- Can drive = has_license AND has_insurance

Test with different combinations.

---

## Exercise 7: Type Conversion
Write a program that:
1. Takes a string number from user (e.g., "42")
2. Convert to integer and print
3. Convert to float and print
4. Check if it's even or odd
5. Print the square of the number

**Expected Output (for input "5"):**
```
Original: 5 (type: <class 'str'>)
As integer: 5 (type: <class 'int'>)
As float: 5.0 (type: <class 'float'>)
Is even: False
Square: 25
```

---

## Exercise 8: Simple Calculator
Write a calculator that:
1. Takes 3 inputs: num1, operator (+, -, *, /), num2
2. Performs the operation
3. Handles division by zero (print "Cannot divide by zero")

**Example:**
```
Enter first number: 10
Enter operator: +
Enter second number: 5
Result: 15
```

---

## Exercise 9: Grade Calculator
Write a program that:
1. Takes marks (0-100) as input
2. Calculates percentage (assume marks out of some total)
3. Assigns grade:
   - 90-100: A
   - 80-89: B
   - 70-79: C
   - 60-69: D
   - Below 60: F
4. Print grade and a comment

---

## Exercise 10: Personal Details Formatter
Create a program that:
1. Takes input: first_name, last_name, email, age
2. Formats and prints in a nice way using f-strings
3. Calculates birth year (current year - age)
4. Prints a nice summary

**Expected Output:**
```
====== PERSONAL DETAILS ======
Name: John Doe
Email: john@example.com
Age: 30 years old
Approximate Birth Year: 1994
===============================
```

---

## Challenge Exercises

### Challenge 1: Number Properties
Write a program that takes a number and prints:
- Is it positive or negative?
- Is it even or odd?
- Is it divisible by 5?
- Its square and square root

### Challenge 2: String Analyzer
Takes a string and prints:
- Length
- Number of spaces
- Number of vowels
- Reversed string
- First and last character

---

## How to Submit Your Work

1. Create `my_solutions.py` in the 01_Basics folder
2. Complete all exercises
3. Test by running: `python my_solutions.py`
4. Make sure output matches expected format
5. Debug any errors using print statements

---

**Next Step:** Once you've completed all exercises and they work correctly, move to Module 2!
