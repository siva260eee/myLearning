# Module 7: Error Handling - Exercises

## Exercise 1: Basic Exception Handling
Write a program that:
1. Takes two numbers from user
2. Divides first by second
3. Handles:
   - ZeroDivisionError
   - ValueError (non-numeric input)
4. Prints result or error message

---

## Exercise 2: Multiple Exception Types
Create function `safe_list_access(lst, index)` that:
1. Returns element at index
2. Handles:
   - IndexError (index out of range)
   - TypeError (not a list)
3. Returns error message or element

---

## Exercise 3: Custom Exception
Create custom exception `NegativeNumberError` and:
1. Raise it when number is negative
2. Catch and handle it
3. Use in a validation function

---

## Exercise 4: Validation Function
Create `validate_user_input(data)` that:
1. Checks name is not empty
2. Checks age is 0-150
3. Checks email has @ symbol
4. Raises ValueError with specific message for each

Test with valid and invalid data.

---

## Exercise 5: File Error Handling
Create function that:
1. Opens a file and reads content
2. Handles FileNotFoundError
3. Handles PermissionError
4. Returns content or None

---

## Exercise 6: Try/Except/Else/Finally
Write a program that:
1. Gets user input
2. Converts to integer
3. Uses try/except/else/finally
4. Each block prints a message

---

## Exercise 7: Nested Exception Handling
Create function with nested try blocks:
```python
def process_data(data):
    try:
        # Outer try
        try:
            # Inner try
            x = int(data)
        except ValueError:
            # Handle inner error
            pass
    except Exception:
        # Handle outer error
        pass
```

---

## Exercise 8: Logging Errors
Create program with logging:
1. Set up logging to file
2. Log different error levels (INFO, WARNING, ERROR)
3. Perform operations and log results
4. Check log file

---

## Exercise 9: Custom Exception Hierarchy
Create exception hierarchy:
```python
class AppError(Exception):
    pass

class ValidationError(AppError):
    pass

class DatabaseError(AppError):
    pass
```

Use in different contexts.

---

## Exercise 10: Defensive Programming
Create robust functions with:
1. Input validation
2. Error handling
3. Informative error messages
4. Graceful degradation

Example: Calculator functions that handle all error cases.

---

## Challenge Exercises

### Challenge 1: Try/Except Practice
Create program that:
1. Reads a CSV file
2. Processes each row
3. Validates data
4. Handles and logs errors
5. Reports on successful/failed rows

### Challenge 2: Error Recovery
Create auto-retry mechanism:
```python
def retry_operation(func, max_attempts=3, delay=1):
    for attempt in range(max_attempts):
        try:
            return func()
        except TemporaryError:
            if attempt < max_attempts - 1:
                time.sleep(delay)
            else:
                raise
```

### Challenge 3: Error Report Generator
Create program that:
1. Catches multiple error types
2. Generates detailed error report
3. Includes:
   - Error type
   - Error message
   - Stack trace
   - Timestamp
   - Recovery suggestion

### Challenge 4: Safe Data Processor
Create processor that:
1. Reads data from multiple sources
2. Validates each item
3. Tracks errors without stopping
4. Reports summary:
   - Items processed
   - Items failed
   - Error types and counts

---

## Debugging Exercise

Find and fix errors:

```python
# Bug 1: Too broad exception
try:
    x = 1 / 0
except:
    print("Error")  # Catches everything!

# Bug 2: Error after exception
try:
    x = int("abc")
except ValueError:
    print(x)  # x doesn't exist if error!

# Bug 3: Missing as
try:
    result = risky_operation()
except Exception e:  # Missing 'as'
    print(e)

# Bug 4: Silencing errors
try:
    data = json.loads(file_content)
except:
    data = {}  # Silently fails if JSON error

# Bug 5: Wrong except order
try:
    operation()
except Exception:  # Too broad, catches all
    print("Error")
except ValueError:  # Never reached!
    print("Value error")
```

---

## How to Submit

1. Create `my_solutions.py` in 07_ErrorHandling folder
2. Complete all exercises
3. Test error conditions thoroughly
4. Include meaningful error messages
5. Use appropriate exception types

---

**Next:** Module 8: Real-World Projects - Apply everything!
