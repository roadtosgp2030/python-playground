# Flashcard Quiz — Build Guide

## What You're Building

A CLI quiz app that stores question/answer pairs, picks them randomly, checks the user's answers, and shows a final score.

## Concepts You'll Practice

- Lists of dicts
- `random` module (`random.shuffle` or `random.sample`)
- `for` loops
- String comparison / normalization (`.lower().strip()`)
- Functions
- f-strings
- File I/O with JSON (stretch goal)

---

## Step-by-Step Plan

### Step 1 — Store flashcards as a list of dicts

```python
flashcards = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 7 * 8?", "answer": "56"},
    {"question": "What keyword starts a function in Python?", "answer": "def"},
]
```

Keep answers lowercase — you'll normalize the user's input to match.

### Step 2 — Shuffle the flashcards

```python
import random
random.shuffle(flashcards)
```

### Step 3 — Loop through and quiz the user

```python
for card in flashcards:
    print(f"Q: {card['question']}")
    user_answer = input("Your answer: ").lower().strip()
    if user_answer == card["answer"]:
        print("Correct!")
    else:
        print(f"Wrong! The answer was: {card['answer']}")
```

### Step 4 — Track the score

Add a `score` counter. Increment it on each correct answer. After the loop, print the final result.

```
You got 4 out of 6 correct! (66.7%)
```

### Step 5 — Wrap in functions

```python
def run_quiz(flashcards: list) -> None:
    ...

def show_score(score: int, total: int) -> None:
    ...

if __name__ == "__main__":
    run_quiz(flashcards)
```

### Step 6 — Allow retrying wrong answers (stretch goal)

After the first pass, collect all cards the user got wrong and offer:
```
You got 2 wrong. Retry them? (y/n):
```
Loop until the user gets them all right or declines.

### Step 7 — Load flashcards from a JSON file (stretch goal)

Move the flashcards into `cards.json` and load them at startup:

```python
import json

with open("cards.json") as f:
    flashcards = json.load(f)
```

This makes it easy to add new cards without touching the code.

---

## Expected Output

```
Flashcard Quiz — 6 questions
------------------------------
Q: What keyword starts a function in Python?
Your answer: def
Correct!

Q: What is the capital of France?
Your answer: Paris
Correct!

Q: What is 7 * 8?
Your answer: 54
Wrong! The answer was: 56

------------------------------
You got 2 out of 3 correct! (66.7%)

Retry wrong answers? (y/n): y

Q: What is 7 * 8?
Your answer: 56
Correct!

All done!
```

---

## File to Create

`quiz.py` — main quiz logic  
`cards.json` — flashcard data (stretch goal)

## Tips

- Use `.lower().strip()` on user input so "Paris" and " paris " both match "paris".
- Get the basic loop working first before adding score tracking or retry logic.
- Pick a topic you're actually studying for the flashcard content — makes it more fun.
