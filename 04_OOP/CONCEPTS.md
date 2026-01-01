# Module 4: Object-Oriented Programming - Concepts

## 1. Classes and Objects

Since you know Java, this will be familiar!

### Python vs Java

**Java:**
```java
public class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() {
        return name;
    }
}

Person p = new Person("Alice", 30);
```

**Python:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name

p = Person("Alice", 30)
```

### Key Differences:
1. No `public`, `private` keywords (use `_` prefix by convention)
2. No type declarations for attributes
3. Constructor is `__init__` (not `Person()`)
4. First parameter is always `self` (like `this` in Java)
5. No `new` keyword - just call the class

## 2. Instance Variables and Methods

```python
class Dog:
    def __init__(self, name, breed):
        # Instance variables (like Java member variables)
        self.name = name
        self.breed = breed
    
    def bark(self):
        # Instance method
        return f"{self.name} says: Woof!"
    
    def describe(self):
        return f"{self.name} is a {self.breed}"

# Create instances
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Labrador")

print(dog1.bark())        # "Buddy says: Woof!"
print(dog2.describe())    # "Max is a Labrador"
print(dog1.name)          # "Buddy"
```

## 3. Encapsulation (Privacy Convention)

Unlike Java, Python doesn't enforce privacy. Use conventions:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Convention: single underscore = "private"
        self.__secret = "hidden" # Double underscore = name mangling (rarely used)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500

# You CAN access _balance (convention only, not enforced)
print(account._balance)  # 1500 - works but shouldn't do this!
```

## 4. Class Variables (Static)

```python
class Student:
    school = "Central High"  # Class variable (shared by all instances)
    student_count = 0
    
    def __init__(self, name):
        self.name = name  # Instance variable
        Student.student_count += 1
    
    def info(self):
        return f"{self.name} from {Student.school}"

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.info())              # "Alice from Central High"
print(Student.student_count)  # 2
print(Student.school)         # "Central High"
```

## 5. Special Methods (Dunder Methods)

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __str__(self):
        # Like toString() in Java
        return f"{self.make} {self.model}"
    
    def __repr__(self):
        # Technical representation (for debugging)
        return f"Car('{self.make}', '{self.model}')"
    
    def __len__(self):
        # For len() function
        return 2  # 2 wheels visible from front :)
    
    def __eq__(self, other):
        # For equality comparison (==)
        return self.make == other.make and self.model == other.model
    
    def __lt__(self, other):
        # For less than (<)
        return self.model < other.model

car1 = Car("Toyota", "Camry")
car2 = Car("Toyota", "Corolla")

print(str(car1))           # "Toyota Camry" (__str__)
print(repr(car1))          # "Car('Toyota', 'Camry')" (__repr__)
print(len(car1))           # 2 (__len__)
print(car1 == car2)        # False (__eq__)
print(car1 < car2)         # False (__lt__)
```

## 6. Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):  # Inherits from Animal
    def speak(self):  # Override method
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # "Buddy says: Woof!"
print(cat.speak())  # "Whiskers says: Meow!"
```

## 7. super() - Call Parent Class

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Call parent constructor
        self.doors = doors
    
    def info(self):
        parent_info = super().info()  # Call parent method
        return f"{parent_info} with {self.doors} doors"

car = Car("Toyota", "Camry", 4)
print(car.info())  # "Toyota Camry with 4 doors"
```

## 8. Multiple Inheritance

```python
class Flyer:
    def fly(self):
        return "Flying..."

class Swimmer:
    def swim(self):
        return "Swimming..."

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())    # "Flying..."
print(duck.swim())   # "Swimming..."
print(duck.quack())  # "Quack!"
```

## 9. Polymorphism

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area()}")
```

## 10. Property Decorators

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property  # Getter
    def celsius(self):
        return self._celsius
    
    @celsius.setter  # Setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Too cold!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)      # 25 (uses @property)
print(temp.fahrenheit)   # 77.0
temp.celsius = 30        # Uses @setter
print(temp.celsius)      # 30
```

---

**Next:** Study examples.py for practical OOP patterns
