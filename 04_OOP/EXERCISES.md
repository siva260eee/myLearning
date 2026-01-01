# Module 4: OOP - Exercises

## Exercise 1: Animal Class Hierarchy

Create an `Animal` base class with:
- `__init__(name)` constructor
- `speak()` method that returns generic sound

Create subclasses:
- `Dog` - returns "Woof!"
- `Cat` - returns "Meow!"
- `Cow` - returns "Moo!"

Test by creating instances and calling speak().

---

## Exercise 2: Bank Account Class

Create a `BankAccount` class:
- Constructor: takes account holder name and initial balance
- Methods:
  - `deposit(amount)` - add to balance
  - `withdraw(amount)` - subtract from balance (check sufficient funds)
  - `get_balance()` - return current balance
  - `transfer(amount, other_account)` - transfer to another account
  - `__str__()` - return account info

Create 2 accounts, deposit, withdraw, and transfer.

---

## Exercise 3: Rectangle Class

Create a `Rectangle` class:
- Constructor: length, width
- Properties:
  - `area` - calculate area (use @property)
  - `perimeter` - calculate perimeter
  - `is_square()` - method to check if square
- Methods:
  - `__str__()` - return "Rectangle: 5x3"
  - `__eq__()` - compare rectangles
  - `resize(new_length, new_width)` - modify dimensions

Create rectangles and test.

---

## Exercise 4: Library Book Class

Create a `Book` class:
- Constructor: title, author, pages, isbn
- Methods:
  - `__str__()` - return book info
  - `is_long()` - return True if pages > 300

Create a `Library` class:
- Constructor: library name
- Methods:
  - `add_book(book)` - add book to library
  - `remove_book(isbn)` - remove by ISBN
  - `search_by_author(author)` - return all books by author
  - `search_by_title(title)` - return book if found
  - `list_all_books()` - display all books

Test with multiple books.

---

## Exercise 5: Employee Class Hierarchy

Create `Employee` base class:
- Constructor: name, employee_id, salary
- Methods:
  - `give_raise(amount)` - increase salary
  - `__str__()` - return employee info

Create subclasses:
- `Manager` - has team_size attribute, override __str__
- `Developer` - has programming_language attribute, override __str__
- `Designer` - has software attribute, override __str__

Create instances and display.

---

## Exercise 6: Shape Hierarchy (Polymorphism)

Create base `Shape` class with area() method.
Create subclasses:
- `Circle` - area = πr²
- `Rectangle` - area = l × w
- `Triangle` - area = 0.5 × b × h

Create a list of different shapes and calculate total area.

---

## Exercise 7: Student Grade Tracker

Create `Student` class:
- Constructor: name, student_id
- Methods:
  - `add_grade(grade)` - store grade
  - `get_average()` - calculate GPA
  - `get_letter_grade()` - return letter grade
  - `__str__()` - return student info

Features:
- Keep track of all students (class variable)
- Get top student
- Get average class GPA

---

## Exercise 8: Temperature Class with Properties

Create `Temperature` class:
- Constructor: celsius value
- Use @property for:
  - celsius (getter/setter with validation)
  - fahrenheit (read-only)
  - kelvin (read-only)

Test conversions and invalid inputs.

---

## Exercise 9: Class Methods and Static Methods

Create a `Person` class:
- Instance: name, age
- Class variable: population
- `__init__()` - increment population
- `class_method birthday_month(month)` - class method
- `static_method is_adult(age)` - static method

Example usage:
```python
p = Person("Alice", 25)
Person.is_adult(25)  # True (static method)
Person.birthday_month(5)  # List people with birthday in May
```

---

## Exercise 10: File Parser Class

Create a `FileReader` class:
- Constructor: filename
- Methods:
  - `read_lines()` - read and return list of lines
  - `count_lines()` - return line count
  - `search(keyword)` - find lines containing keyword

Create a file and test reading/searching.

---

## Challenge Exercises

### Challenge 1: Game Character Class

```python
class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def take_damage(self, damage):
        # Calculate actual damage with defense
        # Reduce hp
        pass
    
    def attack_enemy(self, enemy):
        # Deal damage to enemy
        pass
    
    def is_alive(self):
        return self.hp > 0
    
    def heal(self, amount):
        # Heal up to max_hp
        pass

class Warrior(Character):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
    
    def power_attack(self, enemy):
        # 1.5x damage
        pass

class Mage(Character):
    def __init__(self, name, hp, attack, defense, mana):
        super().__init__(name, hp, attack, defense)
        self.mana = mana
    
    def cast_spell(self, enemy):
        # Use mana, deal extra damage
        pass
```

Create characters and simulate combat!

### Challenge 2: Inventory System

```python
class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

class Inventory:
    def __init__(self, max_weight=100):
        self.items = []
        self.max_weight = max_weight
    
    def add_item(self, item):
        # Check weight limit
        pass
    
    def remove_item(self, name):
        pass
    
    def get_total_value(self):
        pass
    
    def get_total_weight(self):
        pass
    
    def list_items(self):
        pass
```

---

## Debugging Exercise

Find and fix the bugs:

```python
class Rectangle:
    def __init__(length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length + self.width
    
    def __str__():
        return f"Rectangle: {self.length}x{self.width}"

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(side, side)

r = Rectangle(5, 3)
print(r.area())  # Should be 15, not 8
print(r)

s = Square(4)
print(s.area())  # Should be 16
```

---

## How to Submit

1. Create `my_solutions.py` in 04_OOP folder
2. Complete all exercises
3. Add docstrings to classes and methods
4. Test thoroughly
5. Make sure inheritance and polymorphism work

---

**Next:** Module 5: Data Structures (Lists, Dicts, Sets, Tuples)
