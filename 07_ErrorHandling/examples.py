# Module 7: Error Handling - Examples

print("=" * 60)
print("1. BASIC TRY/EXCEPT")
print("=" * 60)

# Simple try/except
try:
    x = 10 / 2
    print(f"10 / 2 = {x}")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Division by zero
try:
    y = 10 / 0
    print(f"10 / 0 = {y}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Type error
try:
    result = "hello" + 5
except TypeError as e:
    print(f"Type error: {e}")

print("\n" + "=" * 60)
print("2. MULTIPLE EXCEPT BLOCKS")
print("=" * 60)

def safe_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid integer")
        return None
    except TypeError:
        print(f"Cannot convert {type(value)} to int")
        return None

print(safe_int("42"))
print(safe_int("abc"))
print(safe_int([1, 2, 3]))

print("\n" + "=" * 60)
print("3. CATCHING MULTIPLE EXCEPTIONS")
print("=" * 60)

def process_value(value):
    try:
        result = 100 / value
        print(f"100 / {value} = {result}")
    except (ValueError, TypeError) as e:
        print(f"Input error: {e}")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

process_value("10")      # Works (string to int)
process_value("abc")     # ValueError
process_value(0)         # ZeroDivisionError

print("\n" + "=" * 60)
print("4. ELSE CLAUSE")
print("=" * 60)

def divide_safe(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
    except TypeError:
        print("Error: Invalid input type")
    else:
        # Only runs if no exception
        print(f"Success: {a} / {b} = {result}")

print("Test 1:")
divide_safe(10, 2)

print("\nTest 2:")
divide_safe(10, 0)

print("\nTest 3:")
divide_safe("10", 2)

print("\n" + "=" * 60)
print("5. FINALLY CLAUSE")
print("=" * 60)

def file_operation():
    try:
        print("Opening file...")
        # Simulating file operation
        raise IOError("File not found")
    except IOError as e:
        print(f"Error: {e}")
    finally:
        print("Cleanup: Closing file...")

file_operation()

print("\n" + "=" * 60)
print("6. RAISING EXCEPTIONS")
print("=" * 60)

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age is unrealistic")
    return True

# Valid age
try:
    validate_age(25)
    print("Age is valid")
except (TypeError, ValueError) as e:
    print(f"Validation error: {e}")

# Invalid ages
print("\nTesting invalid ages:")
for test_age in [-5, 200, "twenty-five"]:
    try:
        validate_age(test_age)
        print(f"{test_age}: Valid")
    except (TypeError, ValueError) as e:
        print(f"{test_age}: Error - {e}")

print("\n" + "=" * 60)
print("7. CUSTOM EXCEPTIONS")
print("=" * 60)

class InsufficientFundsError(Exception):
    """Raised when account balance is insufficient"""
    pass

class InvalidAmountError(Exception):
    """Raised when amount is invalid"""
    pass

def withdraw(account, amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be positive")
    if amount > account["balance"]:
        raise InsufficientFundsError(
            f"Insufficient funds. Balance: ${account['balance']}, Requested: ${amount}"
        )
    account["balance"] -= amount
    return account["balance"]

account = {"name": "Alice", "balance": 1000}

print(f"Initial balance: ${account['balance']}")

# Valid withdrawal
try:
    new_balance = withdraw(account, 200)
    print(f"Withdrew $200, new balance: ${new_balance}")
except (InsufficientFundsError, InvalidAmountError) as e:
    print(f"Error: {e}")

# Invalid withdrawal
try:
    new_balance = withdraw(account, 2000)
    print(f"Withdrew $2000, new balance: ${new_balance}")
except (InsufficientFundsError, InvalidAmountError) as e:
    print(f"Error: {e}")

# Invalid amount
try:
    new_balance = withdraw(account, -50)
    print(f"Withdrew $-50, new balance: ${new_balance}")
except (InsufficientFundsError, InvalidAmountError) as e:
    print(f"Error: {e}")

print("\n" + "=" * 60)
print("8. EXCEPTION INFO WITH 'as e'")
print("=" * 60)

try:
    nums = [1, 2, 3]
    print(nums[10])
except IndexError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
    print(f"Error args: {e.args}")

print("\n" + "=" * 60)
print("9. GENERIC EXCEPTION (CATCH-ALL)")
print("=" * 60)

def risky_operation(operation):
    try:
        if operation == "divide":
            return 10 / 0
        elif operation == "index":
            lst = [1, 2, 3]
            return lst[10]
        elif operation == "key":
            d = {"a": 1}
            return d["b"]
    except ZeroDivisionError:
        print("Division by zero")
    except IndexError:
        print("Index out of range")
    except KeyError:
        print("Key not found")
    except Exception as e:
        print(f"Unknown error: {type(e).__name__}: {e}")
    finally:
        print("Operation completed")

for op in ["divide", "index", "key", "unknown"]:
    print(f"\nOperation: {op}")
    risky_operation(op)

print("\n" + "=" * 60)
print("10. CONTEXT MANAGERS (WITH STATEMENT)")
print("=" * 60)

# File context manager (automatic closing)
print("Writing to file...")
with open("test_file.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

print("Reading from file...")
with open("test_file.txt", "r") as f:
    content = f.read()
    print(f"Content:\n{content}")

print("File automatically closed after 'with' block")

# Custom context manager
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def __enter__(self):
        print(f"Connecting to database: {self.db_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}")
        if exc_type is not None:
            print(f"Error occurred: {exc_type.__name__}: {exc_val}")
        return False  # Don't suppress exception

print("\nUsing custom context manager:")
with DatabaseConnection("mydb") as db:
    print("Performing database operations...")

print("\n" + "=" * 60)
print("11. DEBUGGING WITH PRINT STATEMENTS")
print("=" * 60)

def calculate_average(numbers):
    print(f"DEBUG: Input numbers: {numbers}")
    
    if not numbers:
        print("DEBUG: Empty list")
        return None
    
    total = sum(numbers)
    print(f"DEBUG: Sum = {total}")
    
    avg = total / len(numbers)
    print(f"DEBUG: Average = {avg}")
    
    return avg

result = calculate_average([10, 20, 30, 40])
print(f"Result: {result}")

print("\n" + "=" * 60)
print("12. ASSERTIONS")
print("=" * 60)

def calculate_grade(score):
    assert isinstance(score, (int, float)), "Score must be a number"
    assert 0 <= score <= 100, f"Score must be 0-100, got {score}"
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

# Valid input
try:
    print(f"Score 95: {calculate_grade(95)}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Invalid input
try:
    print(f"Score -5: {calculate_grade(-5)}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

print("\n" + "=" * 60)
print("13. CLEANUP")
print("=" * 60)

import os
if os.path.exists("test_file.txt"):
    os.remove("test_file.txt")
    print("Cleaned up test file")

print("\n" + "=" * 60)
print("END OF EXAMPLES")
print("=" * 60)
