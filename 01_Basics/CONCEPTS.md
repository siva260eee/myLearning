# Module 1: Basics - Concepts

## 1. Variables and Data Types

### Python vs Java

| Java | Python | Notes |
|------|--------|-------|
| `int x = 5;` | `x = 5` | No type declaration needed (dynamic typing) |
| `String name = "John";` | `name = "John"` | Everything's an object, no distinction |
| `double price = 19.99;` | `price = 19.99` | Python infers float type |
| `boolean flag = true;` | `flag = True` | Capital T! |

### Key Python Data Types

1. **Numbers**
   - `int`: 42, -10, 0
   - `float`: 3.14, -2.5, 1.0
   - `complex`: 3+4j (rarely used)

2. **Strings**
   - Single quotes: `'hello'`
   - Double quotes: `"hello"`
   - Triple quotes: `'''multi\nline'''`

3. **Booleans**
   - `True` or `False` (capital letters!)
   - Result of comparisons: `5 > 3` → `True`

4. **Special Type**
   - `None`: Python's null/void (like Java's `null`)

### Dynamic Typing

```python
x = 5          # x is an int
x = "hello"    # NOW x is a string! (allowed in Python)
x = 3.14       # NOW x is a float!
```

This is different from Java where type is fixed!

## 2. Operators

### Arithmetic Operators
- `+` Addition: `3 + 2` → 5
- `-` Subtraction: `5 - 2` → 3
- `*` Multiplication: `4 * 3` → 12
- `/` Division: `10 / 3` → 3.333... (always returns float)
- `//` Floor Division: `10 // 3` → 3 (returns int)
- `%` Modulo: `10 % 3` → 1
- `**` Exponentiation: `2 ** 3` → 8

### Comparison Operators
- `==` Equal to (like Java's `==`)
- `!=` Not equal to
- `<`, `>`, `<=`, `>=`

### Logical Operators
- `and`: Both conditions true (like Java's `&&`)
- `or`: At least one true (like Java's `||`)
- `not`: Negation (like Java's `!`)

### Assignment Operators
- `=` Assignment
- `+=`: `x += 5` means `x = x + 5`
- `-=`, `*=`, `/=`, etc.

## 3. String Operations

Strings are immutable (like Java)

```python
name = "Python"
print(name[0])      # 'P' - indexing (0-based like Java)
print(name[1:3])    # 'yth' - slicing (start:end, end excluded)
print(name[-1])     # 'n' - negative indexing from end
print(len(name))    # 6 - length
```

**String Methods** (no `length()` like Java, use `len()`)
```python
text = "Hello World"
text.lower()        # "hello world"
text.upper()        # "HELLO WORLD"
text.replace("World", "Python")  # "Hello Python"
text.split(" ")     # ["Hello", "World"]
"," .join(["a", "b", "c"])  # "a,b,c"
```

## 4. Type Casting

```python
int("42")      # String to int
float("3.14")  # String to float
str(42)        # Int to string
bool(1)        # Int to boolean (0→False, else→True)
```

## 5. Input and Output

```python
# Output (like System.out.println in Java)
print("Hello, World!")
print(5, 10, 15)  # Prints: 5 10 15
print(f"Name: {name}, Age: {age}")  # f-string (formatted string)

# Input (like Scanner in Java)
name = input("Enter your name: ")  # Returns a string
age = int(input("Enter age: "))    # Convert to int
```

## 6. Comments

```python
# Single line comment (like Java's //)
x = 5  # This is also a comment

"""
This is a multi-line comment
or docstring (like Java's /** */)
"""
```

---

**Next:** Go to examples.py and study the code examples. Then solve exercises in EXERCISES.md
