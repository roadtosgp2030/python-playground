# Number Guessing Game — Build Guide

## What You're Building

A CLI game where the computer picks a random number and the player tries to guess it. The game gives hints ("too high" / "too low") until the player gets it right.

## Concepts You'll Practice

- `random` module
- `while` loops
- `if / elif / else` conditionals
- User input and type conversion (`int()`)
- Functions
- Basic error handling (`try / except`)

---

## Step-by-Step Plan

### Step 1 — Generate a random number

```python
import random
secret = random.randint(1, 100)
```

### Step 2 — Ask the player to guess in a loop

Use a `while True` loop and break out when the guess is correct.

```python
while True:
    guess = input("Guess a number (1-100): ")
    # convert and compare here
```

### Step 3 — Give hints

```
if guess < secret  → print "Too low!"
if guess > secret  → print "Too high!"
if guess == secret → print "Correct!" and break
```

### Step 4 — Count attempts

Add an `attempts` counter that increments each loop iteration. Show it when the player wins.

### Step 5 — Handle bad input

Wrap `int(input(...))` in a `try / except ValueError` so the game doesn't crash on non-numeric input.

### Step 6 — Wrap everything in functions

```python
def get_guess() -> int:
    ...

def play():
    ...

if __name__ == "__main__":
    play()
```

### Step 7 — Add a difficulty setting (stretch goal)

Let the player choose Easy / Medium / Hard, which changes the number range:
- Easy: 1–50
- Medium: 1–100
- Hard: 1–500

### Step 8 — Play again (stretch goal)

After winning, ask "Play again? (y/n)" and restart or exit accordingly.

---

## Expected Output

```
Welcome to the Number Guessing Game!
Difficulty: Medium (1-100)

Guess a number: 50
Too high!

Guess a number: 25
Too low!

Guess a number: 37
Correct! You got it in 3 attempts.

Play again? (y/n):
```

---

## File to Create

`game.py` — put all your code here.

## Tips

- Get a basic version working first, then add stretch goals one at a time.
- Test edge cases: what if the user types "abc"? What if they guess the number on the first try?
