# Module 3: Functions - Examples

print("=" * 60)
print("1. BASIC FUNCTION DEFINITION AND CALLING")
print("=" * 60)

def greet():
    print("Hello, World!")

greet()

def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

def greet_person(name):
    return f"Hello, {name}!"

message = greet_person("Alice")
print(message)

print("\n" + "=" * 60)
print("2. FUNCTIONS WITH MULTIPLE RETURN VALUES")
print("=" * 60)

def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([5, 2, 9, 1, 7])
print(f"Min: {min_val}, Max: {max_val}")

def swap(a, b):
    return b, a

x, y = 10, 20
print(f"Before: x={x}, y={y}")
x, y = swap(x, y)
print(f"After: x={x}, y={y}")

print("\n" + "=" * 60)
print("3. DEFAULT PARAMETERS")
print("=" * 60)

def power(base, exponent=2):
    return base ** exponent

print(f"2^2 = {power(2)}")      # Uses default exponent=2
print(f"2^3 = {power(2, 3)}")   # Overrides default
print(f"5^2 = {power(5)}")

def create_profile(name, age=0, city="Unknown"):
    return f"{name} ({age}) from {city}"

print(create_profile("Bob"))
print(create_profile("Bob", 25))
print(create_profile("Bob", 25, "NYC"))

print("\n" + "=" * 60)
print("4. NAMED ARGUMENTS (KEYWORD ARGUMENTS)")
print("=" * 60)

def order_pizza(size, crust="thin", toppings="cheese"):
    return f"Pizza: {size} size, {crust} crust, {toppings}"

print(order_pizza("large"))
print(order_pizza("medium", crust="thick"))
print(order_pizza("small", toppings="pepperoni", crust="stuffed"))
print(order_pizza(size="large", toppings="mushroom"))

print("\n" + "=" * 60)
print("5. *ARGS - VARIABLE POSITIONAL ARGUMENTS")
print("=" * 60)

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
print(f"sum_all(10) = {sum_all(10)}")

def print_items(*items):
    print(f"Items: {items}")
    for item in items:
        print(f"  - {item}")

print_items("apple", "banana", "cherry")

print("\n" + "=" * 60)
print("6. **KWARGS - VARIABLE KEYWORD ARGUMENTS")
print("=" * 60)

def print_info(**info):
    print("Information:")
    for key, value in info.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=30, city="NYC", job="Engineer")

def create_user(username, **details):
    print(f"Creating user: {username}")
    for key, value in details.items():
        print(f"  {key}: {value}")

create_user("john_doe", email="john@example.com", age=25, active=True)

print("\n" + "=" * 60)
print("7. COMBINING *ARGS AND **KWARGS")
print("=" * 60)

def flexible_function(a, b, *args, **kwargs):
    print(f"Regular: a={a}, b={b}")
    print(f"Variable positional: {args}")
    print(f"Variable keyword: {kwargs}")

flexible_function(1, 2, 3, 4, 5, x=10, y=20, z=30)

print("\n" + "=" * 60)
print("8. DOCSTRINGS")
print("=" * 60)

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): Length of the rectangle
        width (float): Width of the rectangle
    
    Returns:
        float: Area of the rectangle
    """
    return length * width

print(f"Area of 5x3 rectangle: {calculate_area(5, 3)}")
print("\nDocstring:")
print(calculate_area.__doc__)

print("\n" + "=" * 60)
print("9. VARIABLE SCOPE")
print("=" * 60)

global_var = "I'm global"

def test_scope():
    local_var = "I'm local"
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")

test_scope()
print(f"Outside function: {global_var}")
# print(f"Outside function: {local_var}")  # This would error!

# Modifying global variable
counter = 0

def increment():
    global counter
    counter += 1
    return counter

print(f"\nCounter: {increment()}")  # 1
print(f"Counter: {increment()}")    # 2
print(f"Counter: {counter}")        # 2

print("\n" + "=" * 60)
print("10. LAMBDA FUNCTIONS")
print("=" * 60)

# Lambda function stored in variable
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

add_func = lambda a, b: a + b
print(f"add_func(3, 4) = {add_func(3, 4)}")

# Lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Lambda with sorted
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_score = sorted(students, key=lambda s: s[1])
print(f"Sorted by score: {sorted_by_score}")

print("\n" + "=" * 60)
print("11. NESTED FUNCTIONS")
print("=" * 60)

def outer(x):
    def inner(y):
        return x + y
    return inner

add_10 = outer(10)
print(f"add_10(5) = {add_10(5)}")  # 15
print(f"add_10(20) = {add_10(20)}")  # 30

print("\n" + "=" * 60)
print("12. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Calculate grade
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

grades = [85, 92, 78, 95, 88]
for grade in grades:
    print(f"Score {grade}: Grade {get_grade(grade)}")

# Example 2: Validate email
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]

emails = ["user@example.com", "invalid.email", "test@domain.org"]
for email in emails:
    print(f"{email}: {is_valid_email(email)}")

print("\n" + "=" * 60)
print("END OF EXAMPLES")
print("=" * 60)
