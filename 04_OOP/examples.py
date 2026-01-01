# Module 4: OOP - Examples

print("=" * 60)
print("1. BASIC CLASS DEFINITION")
print("=" * 60)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    def have_birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age}"

person1 = Person("Alice", 30)
print(person1.greet())
print(person1.have_birthday())
print(person1.greet())

person2 = Person("Bob", 25)
print(person2.greet())

print("\n" + "=" * 60)
print("2. CLASS VARIABLES (SHARED)")
print("=" * 60)

class Student:
    school = "Central High"  # Class variable
    total_students = 0
    
    def __init__(self, name):
        self.name = name  # Instance variable
        Student.total_students += 1
    
    def info(self):
        return f"{self.name} from {Student.school}"

s1 = Student("Alice")
s2 = Student("Bob")
s3 = Student("Charlie")

print(s1.info())
print(f"Total students: {Student.total_students}")

# Change class variable
Student.school = "North High"
print(f"New school: {s1.info()}")

print("\n" + "=" * 60)
print("3. SPECIAL METHODS (__str__, __repr__, etc.)")
print("=" * 60)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def __str__(self):
        # Used by print() and str()
        return f"{self.year} {self.make} {self.model}"
    
    def __repr__(self):
        # Used by repr() - for debugging
        return f"Car('{self.make}', '{self.model}', {self.year})"
    
    def __eq__(self, other):
        # Comparison: ==
        return (self.make == other.make and 
                self.model == other.model and 
                self.year == other.year)
    
    def __lt__(self, other):
        # Less than: <
        return self.year < other.year

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)
car3 = Car("Toyota", "Camry", 2020)

print(f"str: {str(car1)}")
print(f"repr: {repr(car1)}")
print(f"car1 == car3: {car1 == car3}")
print(f"car1 < car2: {car1 < car2}")

print("\n" + "=" * 60)
print("4. INHERITANCE")
print("=" * 60)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):  # Override
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):  # Override
        return f"{self.name} says: Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
animal = Animal("Generic")

print(dog.speak())
print(cat.speak())
print(animal.speak())

print("\n" + "=" * 60)
print("5. SUPER() - CALL PARENT")
print("=" * 60)

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def info(self):
        return f"{self.make} {self.model}"

class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar
    
    def info(self):
        parent_info = super().info()
        sidecar = "with sidecar" if self.has_sidecar else "no sidecar"
        return f"{parent_info} ({sidecar})"

moto = Motorcycle("Harley", "Davidson", True)
print(moto.info())

print("\n" + "=" * 60)
print("6. POLYMORPHISM")
print("=" * 60)

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4)
]

print("Calculating areas:")
for shape in shapes:
    print(f"{shape.__class__.__name__}: {shape.area():.2f}")

print("\n" + "=" * 60)
print("7. ENCAPSULATION (PRIVACY BY CONVENTION)")
print("=" * 60)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # Convention: "private"
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self._balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: ${account.get_balance()}")

print("\n" + "=" * 60)
print("8. PROPERTY DECORATORS")
print("=" * 60)

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Convert to Fahrenheit"""
        return self._celsius * 9/5 + 32
    
    @property
    def kelvin(self):
        """Convert to Kelvin"""
        return self._celsius + 273.15

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

temp.celsius = 0
print(f"\nAfter setting to 0:")
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")

print("\n" + "=" * 60)
print("9. MULTIPLE INHERITANCE")
print("=" * 60)

class Flyer:
    def fly(self):
        return "Flying through the sky"

class Swimmer:
    def swim(self):
        return "Swimming in water"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack! Quack!"

duck = Duck()
print(duck.fly())
print(duck.swim())
print(duck.quack())

print("\n" + "=" * 60)
print("10. PRACTICAL EXAMPLE: STUDENT CLASS")
print("=" * 60)

class StudentFull:
    total_students = 0
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
        StudentFull.total_students += 1
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        else:
            return "F"
    
    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"
    
    def __repr__(self):
        return f"StudentFull('{self.name}', {self.student_id})"
    
    @staticmethod
    def from_string(data):
        # Factory method
        name, student_id = data.split(",")
        return StudentFull(name, int(student_id))

s1 = StudentFull("Alice", 101)
s1.add_grade(85)
s1.add_grade(92)
s1.add_grade(88)

s2 = StudentFull("Bob", 102)
s2.add_grade(78)
s2.add_grade(81)

print(f"{s1}: Average {s1.get_average():.2f}, Grade {s1.get_letter_grade()}")
print(f"{s2}: Average {s2.get_average():.2f}, Grade {s2.get_letter_grade()}")
print(f"Total students: {StudentFull.total_students}")

print("\n" + "=" * 60)
print("END OF EXAMPLES")
print("=" * 60)
