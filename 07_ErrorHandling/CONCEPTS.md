# Module 7: Error Handling - Concepts

## 1. Exception Types

Python has built-in exception types (similar to Java):

```python
# Common exceptions
TypeError        # Wrong type (e.g., int + string)
ValueError       # Wrong value (e.g., int("abc"))
KeyError        # Dictionary key not found
IndexError      # List index out of range
FileNotFoundError # File doesn't exist
ZeroDivisionError # Division by zero
AttributeError  # Object attribute doesn't exist
NameError       # Variable not defined
IOError         # Input/output error
ImportError     # Module not found
```

## 2. try/except Block

### Basic Structure

```python
try:
    # Code that might cause error
    result = 10 / 0
except ZeroDivisionError:
    # Handle this specific error
    print("Cannot divide by zero!")

# Multiple except blocks
try:
    value = int(input("Enter number: "))
    result = 10 / value
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Catching Multiple Exceptions

```python
try:
    # Code
    pass
except (ValueError, TypeError):
    # Handles both ValueError and TypeError
    print("Bad input!")

# Generic exception (catches everything)
try:
    # Code
    pass
except Exception as e:
    print(f"Error: {e}")
```

## 3. else and finally

```python
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    # Runs if NO exception occurred
    print(f"Result: {result}")
finally:
    # Always runs (like Java finally)
    print("Cleanup code here")
```

## 4. Raising Exceptions

```python
# Raise custom exception
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems too high")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

# Raise with message
def withdraw(account, amount):
    if amount > account["balance"]:
        raise ValueError(f"Insufficient funds. Balance: {account['balance']}")
    account["balance"] -= amount
    return account["balance"]
```

## 5. Custom Exceptions

Create your own exception classes:

```python
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    pass

class InvalidAgeError(Exception):
    """Raised when age is invalid"""
    pass

def withdraw_money(account, amount):
    if amount > account["balance"]:
        raise InsufficientFundsError(f"Need ${amount}, but only have ${account['balance']}")

try:
    withdraw_money({"balance": 100}, 150)
except InsufficientFundsError as e:
    print(f"Error: {e}")
```

## 6. Debugging Techniques

### Using print() for debugging

```python
def calculate(x, y):
    print(f"DEBUG: x={x}, y={y}")  # Check inputs
    result = x + y
    print(f"DEBUG: result={result}")  # Check calculation
    return result
```

### Using assert() for validation

```python
def calculate_grade(score):
    assert isinstance(score, (int, float)), "Score must be a number"
    assert 0 <= score <= 100, "Score must be 0-100"
    
    if score >= 90:
        return "A"
    # ... rest of code

calculate_grade(-5)  # AssertionError: Score must be 0-100
```

### Using traceback

```python
import traceback

try:
    # Code that might error
    data = {"key": "value"}
    print(data["missing"])
except KeyError:
    traceback.print_exc()  # Print full traceback
```

### Using logging (better than print)

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def divide(a, b):
    logger.info(f"Dividing {a} by {b}")
    try:
        result = a / b
        logger.info(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero attempted")
        return None
```

## 7. Context Managers

Automatically handle setup and cleanup:

```python
# With statement (like Java try-with-resources)
with open("file.txt", "r") as f:
    content = f.read()
# File automatically closed

# Custom context manager
class DatabaseConnection:
    def __enter__(self):
        print("Connecting to database...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection...")
        # Cleanup code

with DatabaseConnection() as db:
    print("Database operations...")
```

## 8. Common Error Patterns

```python
# Bad: Silent failures
result = None
try:
    result = risky_operation()
except:  # Catches everything silently!
    pass

# Better: Specific exception handling
try:
    result = risky_operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    result = default_value
except IOError as e:
    logger.error(f"IO error: {e}")
    raise  # Re-raise for caller to handle

# Bad: Catching too broad
try:
    x = 1 / 0
except:  # Too broad!
    print("Error occurred")

# Better: Specific exception
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

**Next:** Study examples.py for practical error handling patterns
