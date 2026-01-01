# Module 2: Control Flow - Exercises

## Exercise 1: Simple Grade Checker
Take a score (0-100) and print the grade:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F

Also print a message for each grade.

---

## Exercise 2: Number Guessing Game
1. Generate a random number between 1 and 100
2. Ask user to guess
3. Tell if their guess is too high or too low
4. Count attempts
5. Print congratulations when they guess correctly
6. Print total attempts

**Hint:** Use `import random` and `random.randint(1, 100)`

---

## Exercise 3: Times Table
Take a number from user and print its multiplication table (1-10)

**Expected Output (for input 5):**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

---

## Exercise 4: Sum of Numbers
Take two numbers from user and print the sum of all numbers between them (inclusive)

**Example (for inputs 3 and 7):**
```
Sum of 3 to 7: 3+4+5+6+7 = 25
```

---

## Exercise 5: Find Prime Number
Write a program that:
1. Takes a number from user
2. Checks if it's prime (divisible only by 1 and itself)
3. Prints "Is Prime" or "Not Prime"

**Hint:** A prime is only divisible evenly by 1 and itself

---

## Exercise 6: Pattern Printing
Print these patterns:

**Pattern A: Triangle**
```
*
**
***
****
*****
```

**Pattern B: Right Triangle**
```
    *
   **
  ***
 ****
*****
```

**Pattern C: Diamond**
```
  *
 * *
* * *
 * *
  *
```

---

## Exercise 7: String Reversal
Take a string and print it reversed character by character

**Example:**
```
Input: "Python"
Output: "nohtyP"
```

Do this TWO ways:
1. Using a for loop
2. Using Python slicing [:]

---

## Exercise 8: Count Vowels and Consonants
Take a string and count:
- Vowels (a, e, i, o, u)
- Consonants
- Spaces

Print the counts

**Example:**
```
Input: "Hello World"
Vowels: 3
Consonants: 7
Spaces: 1
```

---

## Exercise 9: Factorial Calculator
Calculate factorial of a number using a loop (not using math library)

Factorial of 5 = 5 × 4 × 3 × 2 × 1 = 120

---

## Exercise 10: FizzBuzz
Classic programming exercise:
- Print numbers 1 to 100
- If divisible by 3: print "Fizz"
- If divisible by 5: print "Buzz"
- If divisible by both: print "FizzBuzz"
- Otherwise: print the number

**Expected Output (partial):**
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
```

---

## Challenge Exercises

### Challenge 1: Number Pyramid
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

### Challenge 2: Perfect Number Checker
A perfect number equals the sum of its divisors (except itself)
Example: 6 = 1 + 2 + 3

Check if a number is perfect.

### Challenge 3: List Comprehension Exercises
1. Create list of squares from 1-10: [1, 4, 9, 16, ...]
2. Create list of even numbers from 1-20: [2, 4, 6, ...]
3. Create list of uppercase from ["hello", "world"]: ["HELLO", "WORLD"]
4. Create list of lengths: ["python"] → [6]

### Challenge 4: Number Guessing Game Advanced
1. Allow user to play multiple rounds
2. Keep high score (fewest attempts)
3. Ask to play again at the end
4. Print statistics (total games, best score)

---

## How to Test
1. Create `my_solutions.py` in 02_Control_Flow folder
2. Complete all exercises
3. Run and verify output
4. Test with different inputs
5. Debug any issues

---

**Next:** Once all exercises work, move to Module 3: Functions!
