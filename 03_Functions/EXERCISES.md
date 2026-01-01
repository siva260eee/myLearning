# Module 3: Functions - Exercises

## Exercise 1: Simple Calculator
Create functions for:
- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)` - handle division by zero

Test each function with sample inputs.

---

## Exercise 2: Temperature Converter
Create two functions:
- `celsius_to_fahrenheit(celsius)` - F = (C × 9/5) + 32
- `fahrenheit_to_celsius(fahrenheit)` - C = (F - 32) × 5/9

Test by converting back and forth.

---

## Exercise 3: String Functions
Create functions:
- `reverse_string(s)` - return reversed string
- `is_palindrome(s)` - check if string reads same forwards and backwards
- `count_vowels(s)` - count vowels
- `capitalize_words(s)` - capitalize first letter of each word

Test with different strings.

---

## Exercise 4: List Functions
Create functions:
- `sum_of_list(lst)` - return sum (or use built-in sum())
- `average(lst)` - return average
- `find_max(lst)` - return max (or use built-in max())
- `find_min(lst)` - return min (or use built-in min())
- `remove_duplicates(lst)` - return list with unique values

Test with: `[1, 2, 2, 3, 3, 3, 4, 5, 5]`

---

## Exercise 5: Using Default Parameters
Create a function:
```python
def greet(name="Guest", greeting="Hello"):
    return f"{greeting}, {name}!"
```

Call it different ways:
- `greet()` → "Hello, Guest!"
- `greet("Alice")` → "Hello, Alice!"
- `greet("Bob", "Hi")` → "Hi, Bob!"
- `greet(greeting="Hey", name="Charlie")` → "Hey, Charlie!"

---

## Exercise 6: *args Example
Create a function that accepts variable arguments:
```python
def list_items(*items):
    # Print each item numbered
```

Test with:
- `list_items("apple")`
- `list_items("apple", "banana", "cherry")`
- `list_items(1, 2, 3, 4, 5)`

---

## Exercise 7: **kwargs Example
Create a function:
```python
def create_profile(name, **info):
    # Print name and all info nicely formatted
```

Test with:
```python
create_profile("Alice", age=30, job="Engineer", city="NYC")
create_profile("Bob", age=25)
```

---

## Exercise 8: Print Report Function
Create function that uses both *args and **kwargs:
```python
def print_report(title, *items, **metadata):
    # Print title
    # Print all items with numbers
    # Print metadata (author, date, etc.)
```

---

## Exercise 9: Grade Validator Function
```python
def validate_grade(grade):
    # Check if grade is valid (0-100)
    # Return True or False
```

Also create:
```python
def get_letter_grade(score):
    # A: 90-100, B: 80-89, etc.
    # Handle invalid scores
```

---

## Exercise 10: Find Functions
Create functions to work with lists:
- `find_index(lst, item)` - return index or -1 if not found
- `find_all_indices(lst, item)` - return list of all indices
- `contains(lst, item)` - return True/False
- `count_occurrences(lst, item)` - return count

Test with: `[1, 2, 3, 2, 4, 2, 5]` looking for `2`

---

## Challenge Exercises

### Challenge 1: Number Analysis
```python
def analyze_numbers(*numbers):
    # Return dictionary with:
    # - sum, average, min, max, count
    # - even_count, odd_count
```

Example:
```python
result = analyze_numbers(1, 2, 3, 4, 5)
# {
#    'sum': 15,
#    'average': 3.0,
#    'min': 1,
#    'max': 5,
#    'count': 5,
#    'even_count': 2,
#    'odd_count': 3
# }
```

### Challenge 2: Filter Numbers
```python
def filter_numbers(numbers, **criteria):
    # criteria might have: min_val, max_val, only_even, only_odd
    # Return filtered list
```

Example:
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_numbers(nums, min_val=3, max_val=8, only_even=True)
# [4, 6, 8]
```

### Challenge 3: Format Data
```python
def format_table(*rows, **options):
    # rows are tuples of data
    # options: title, separator, alignment
    # Return formatted table
```

### Challenge 4: Lambda Exercises
1. Create lambda to double a number: `double = lambda x: ...`
2. Create lambda for max of two: `max_of_two = lambda x, y: ...`
3. Sort list of tuples by second element using lambda
4. Filter list keeping only strings with 'a' using lambda

---

## Debugging Exercise

Here's code with bugs - find and fix them:

```python
def calculate(a, b, operation="add"):
    if operation == "add"
        return a + b
    elif operation = "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide"
        if b = 0:
            return "Cannot divide by zero"
        return a / b

result = calculate(10, 5)
print(f"Result: {result}")
```

---

## How to Submit
1. Create `my_solutions.py` in 03_Functions folder
2. Complete all exercises
3. Add docstrings to each function
4. Test thoroughly
5. Fix any bugs

---

**Next:** Move to Module 4: Object-Oriented Programming (OOP) - this uses Java patterns!
