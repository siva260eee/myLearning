def test_exercise1():
    """Test Exercise 1"""
    name = "Shiva"
    age = 25
    height = 1.75
    whether_u_code = True
    
    output = f"My name is {name}\nI am {age} years old\nMy height is {height} meters\nI code: {whether_u_code}"
    
    assert "Shiva" in output
    assert "25" in output
    assert "1.75" in output
    assert "True" in output

def test_arithmetic():
    """Test Exercise 2"""
    a, b = 10, 3
    
    assert a + b == 13
    assert a - b == 7
    assert a * b == 30
    assert a // b == 3
    assert a % b == 1

def test_temperature():
    """Test Exercise 4"""
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    
    assert abs(fahrenheit - 77.0) < 0.01