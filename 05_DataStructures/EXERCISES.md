# Module 5: Data Structures - Exercises

## Exercise 1: List Operations
Create a list of 10 numbers and perform:
1. Sort ascending and descending
2. Find min, max, sum, average
3. Remove duplicates
4. Find index of largest value
5. Slice first 5 and last 5 elements

---

## Exercise 2: List Comprehension
Create these lists using comprehension:
1. Squares of numbers 1-10
2. Even numbers 1-20
3. Uppercase of words: ["hello", "world", "python"]
4. Lengths of words: ["a", "abc", "ab"] → [1, 3, 2]
5. Filtered: numbers 1-20 that are divisible by 3

---

## Exercise 3: Tuple Unpacking
Create functions:
- `get_coordinates()` - return tuple (x, y)
- `get_rgb()` - return tuple (r, g, b)

Use unpacking in main code:
```python
x, y = get_coordinates()
r, g, b = get_rgb()
```

---

## Exercise 4: Set Operations
Create two sets of students:
- Set A: ["Alice", "Bob", "Charlie", "David"]
- Set B: ["Bob", "Charlie", "Eve", "Frank"]

Find:
1. Students in both sets (intersection)
2. All students (union)
3. Students only in A (difference)
4. Students unique to each set (symmetric difference)

---

## Exercise 5: Dictionary Basics
Create a dictionary of student grades:
```python
grades = {
    "Alice": [85, 92, 88],
    "Bob": [78, 81, 76],
    "Charlie": [95, 98, 92]
}
```

1. Calculate average for each student
2. Find top student
3. Add new student
4. Update grades
5. Remove a student
6. Print all in formatted way

---

## Exercise 6: Word Counter
Write a function that:
1. Takes a string
2. Returns dictionary with word counts
3. Sorts by frequency

Example:
```python
text = "hello world hello python hello"
# Result: {"hello": 3, "world": 1, "python": 1}
```

---

## Exercise 7: List of Dictionaries
Create a list of books:
```python
books = [
    {"title": "Python 101", "author": "John", "pages": 300},
    {"title": "Java Guide", "author": "Jane", "pages": 500},
    {"title": "Web Dev", "author": "Jack", "pages": 250}
]
```

1. Find book with most pages
2. List all titles
3. List authors
4. Search by author
5. Add new book
6. Sort by pages

---

## Exercise 8: Data Structure Conversion
Convert between data structures:
1. List to tuple
2. Tuple to list
3. List to set (remove duplicates)
4. Dictionary keys/values to list
5. List of pairs to dictionary

---

## Exercise 9: Find Duplicates
Write function to:
1. Find duplicate items in list
2. Count occurrences
3. Return unique items with counts as dict

Example:
```python
nums = [1, 2, 2, 3, 3, 3, 4, 4]
# Result: {1: 1, 2: 2, 3: 3, 4: 2}
```

---

## Exercise 10: Merge and Flatten
1. Merge two lists
2. Merge two dictionaries
3. Flatten nested list (convert [[1,2], [3,4]] to [1,2,3,4])
4. Create nested structure (list of dicts in dict)

---

## Challenge Exercises

### Challenge 1: Inventory System
```python
inventory = {
    "apple": {"price": 0.50, "quantity": 10},
    "banana": {"price": 0.30, "quantity": 5},
    "orange": {"price": 0.75, "quantity": 8}
}
```

Functions:
- `total_value()` - total inventory value
- `add_stock(item, quantity)`
- `remove_stock(item, quantity)`
- `list_items()` - formatted display
- `search(item)` - find and display

### Challenge 2: File Word Frequency
1. Read a file
2. Split into words
3. Count word frequency
4. Display top 10 most common words
5. Save results to file

### Challenge 3: Student Management
Create system to manage students:
- Add/remove students
- Add/remove grades
- Calculate GPA
- Find students by criteria (GPA > 3.5)
- Export to formatted report

### Challenge 4: N-gram Generator
Create function that:
- Takes text and n (number)
- Returns dictionary of n-grams with counts

Example (n=2, text="the cat in the hat"):
```python
{
    "the cat": 1,
    "cat in": 1,
    "in the": 1,
    "the hat": 1
}
```

---

## Debugging Exercise

Find and fix bugs:

```python
# Bug 1: Wrong access
person = {"name": "Alice", "age": 30}
print(person.name)  # Should use ["name"]

# Bug 2: Modifying tuple
point = (1, 2)
point[0] = 5  # Error - tuples immutable

# Bug 3: Set comprehension (wrong syntax)
evens = {x for x in range(10) if x % 2}  # Should be ==

# Bug 4: Dictionary duplicate keys
data = {"a": 1, "b": 2, "a": 3}  # Second "a" overwrites first

# Bug 5: List vs list element
numbers = [1, 2, 3]
result = numbers.sort()  # Returns None, doesn't return sorted list
```

---

## How to Submit

1. Create `my_solutions.py` in 05_DataStructures folder
2. Complete all exercises
3. Test with different inputs
4. Handle edge cases
5. Add comments explaining logic

---

**Next:** Module 6: File I/O and Working with Files
