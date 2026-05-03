# Simple Calculator — Build Guide

## What You're Building

A CLI calculator that takes two numbers and an operator from the user, performs the calculation, and loops until the user decides to quit.

## Concepts You'll Practice

- Functions
- `while` loops
- `if / elif / else` conditionals
- User input and type conversion (`float()`)
- Error handling (`try / except`, division by zero)
- f-strings for output formatting

---

## Step-by-Step Plan

### Step 1 — Build one function per operation

Each function takes two numbers and returns a result.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
```

### Step 2 — Ask the user for input

```python
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
```

### Step 3 — Route to the right function

Use `if / elif / else` to call the correct function based on the operator.

```python
if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    ...
```

### Step 4 — Handle errors

Two things can go wrong:
- User types a letter instead of a number → catch `ValueError`
- User divides by zero → catch `ZeroDivisionError`

```python
try:
    num1 = float(input("Enter first number: "))
except ValueError:
    print("That's not a valid number.")
```

### Step 5 — Loop until the user quits

Wrap the whole thing in a `while True` loop. At the end of each calculation, ask:

```
Calculate again? (y/n):
```

Break the loop if the user types `n`.

### Step 6 — Wrap everything in a `main()` function

```python
def main():
    print("Simple Calculator")
    while True:
        ...

if __name__ == "__main__":
    main()
```

### Step 7 — Use the previous result (stretch goal)

After each calculation, ask:
```
Use result (42.0) as first number? (y/n):
```
If yes, skip asking for the first number and reuse the last result.

---

## Expected Output

```
Simple Calculator
------------------
Enter first number: 10
Enter operator (+, -, *, /): *
Enter second number: 5
Result: 10.0 * 5.0 = 50.0

Calculate again? (y/n): y

Enter first number: 100
Enter operator (+, -, *, /): /
Enter second number: 0
Error: Cannot divide by zero.

Calculate again? (y/n): n
Goodbye!
```

---

## File to Create

`calculator.py` — put all your code here.

## Tips

- Build Steps 1–3 first and make sure basic math works before adding error handling.
- Test each operator one by one.
- Try typing "abc" as a number to make sure your error handling works.
