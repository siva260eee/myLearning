
def exercise_1():
    """Exercise 1: Variables and Data Types"""
    name ="Shiva"
    age = 25
    height = 5.9
    whether_u_code = True
    print(f"My Name is : {name}")
    print(f"I am  {age} years old") 
    print(f"My Height is {height} feet")
    print(f"Whether I code: {whether_u_code}")
    return {
        'name': name,
        'age': age,
        'height': height,
        'code': whether_u_code
    }



def exercise_2():
    """Exercise 2: Arithmetic Operations"""
    a = 10
    b = 3
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    floor_division = a // b
    modulo = a % b
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Floor Division: {floor_division}")
    print(f"Modulo: {modulo}")
    return {
        'addition': addition,
        'subtraction': subtraction,
        'multiplication': multiplication,
        'floor_division': floor_division,
        'modulo': modulo
    }


def exercise_3():
    """Exercise 3: String Manipulations"""
    my_string = input("Enter a string: ")
    
    length = len(my_string)
    first_3 = my_string[:3]
    last_5 = my_string[-5:]
    uppercased = my_string.upper()
    lowercased = my_string.lower()
    replaced = my_string.replace("Python", "Java")
    contains_program = "Program" in my_string
    
    print(f"Length: {length}")
    print(f"First 3 characters: {first_3}")
    print(f"Last 5 characters: {last_5}")
    print(f"Uppercase: {uppercased}")
    print(f"Lowercase: {lowercased}")
    print(f"Replaced: {replaced}")
    print(f"Contains 'Program': {contains_program}")
    
    return {
        'length': length,
        'first_3': first_3,
        'last_5': last_5,
        'uppercased': uppercased,
        'lowercased': lowercased,
        'replaced': replaced,
        'contains_program': contains_program
    }

def exercise_4():
    """Exercise 3: Temperature Conversion"""
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
    return fahrenheit


def exercise_5():  
    ## Exercise 5: Age Category
    age = int(input("Enter your age: "))
    if age < 13:
        category = "Child"
    elif 13 <= age < 18:
        category = "Teen"
    elif 18 <= age < 65:
        category = "Adult"
    else:
        category = "Senior"
    
    print(f"Age Category: {category}")
    return category

def main():
    # """Run all exercises"""
    # print("=" * 50)
    # print("EXERCISE 1: Variables and Data Types")
    # print("=" * 50)
    # result1 = exercise_1()
    
    # print("\n" + "=" * 50)
    # print("EXERCISE 2: Arithmetic Operations")
    # print("=" * 50)
    # result2 = exercise_2()
    
    # print("\n" + "=" * 50)
    # print("EXERCISE 3: String Manipulations")
    # print("=" * 50)
    # result3 = exercise_3()
    
    # print("\n" + "=" * 50)
    # print("EXERCISE 4: Temperature Conversion")
    # print("=" * 50)
    # result4 = exercise_4()
    
    # print("\n" + "=" * 50)
    # print("ALL EXERCISES COMPLETED")
    # print("=" * 50)

if __name__ == '__main__':
    main()