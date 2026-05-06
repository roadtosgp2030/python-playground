# Word Counter — Build Guide

## What You're Building

A CLI tool that reads text (typed by the user or loaded from a `.txt` file), then reports:
- Total word count
- Unique word count
- Top 5 most frequent words

## Concepts You'll Practice

- String methods (`.split()`, `.lower()`, `.strip()`, `.punctuation`)
- Dicts and dict sorting
- `collections.Counter` (built-in, very useful)
- File I/O (`open`, `read`)
- Functions
- `pathlib` for file paths (stretch goal)

---

## Step-by-Step Plan

### Step 1 — Get text from the user

Start simple: just ask for a sentence via `input()`.

```python
text = input("Enter text: ")
```

### Step 2 — Split into words and count

```python
words = text.lower().split()
total = len(words)
unique = len(set(words))
```

### Step 3 — Count word frequency with a dict

```python
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
```

Or use the shortcut:
```python
from collections import Counter
frequency = Counter(words)
```

### Step 4 — Show top 5 most frequent words

```python
top5 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:5]
for word, count in top5:
    print(f"  {word}: {count}")
```

### Step 5 — Strip punctuation from words

"hello," and "hello" should count as the same word. Use `str.strip()` with `string.punctuation`:

```python
import string
words = [word.strip(string.punctuation) for word in text.lower().split()]
words = [w for w in words if w]  # remove empty strings
```

### Step 6 — Load from a .txt file (stretch goal)

Instead of typing text, let the user provide a file path:

```python
path = input("Enter file path (or press Enter to type text): ").strip()
if path:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
else:
    text = input("Enter text: ")
```

### Step 7 — Wrap everything in functions

```python
def clean_words(text: str) -> list[str]:
    ...

def count_words(words: list[str]) -> dict:
    ...

def show_report(words: list[str], frequency: dict) -> None:
    ...

def main():
    ...

if __name__ == "__main__":
    main()
```

### Step 8 — Save report to a file (stretch goal)

After showing the report, ask:
```
Save report to file? (y/n):
```
Write the results to `report.txt` using `open("report.txt", "w")`.

---

## Expected Output

```
Word Counter
------------
Source: sample.txt

Total words:   120
Unique words:  74

Top 5 most frequent words:
  the: 10
  and: 8
  is: 6
  to: 5
  a: 4

Save report to file? (y/n): y
Report saved to report.txt
```

---

## Files to Create

`counter.py` — main logic  
`sample.txt` — a sample text file to test with (copy any paragraph from the web)

## Tips

- Use `collections.Counter` — it does Step 3 in one line and has a built-in `.most_common(5)` method.
- Common words like "the", "a", "is" will always dominate. That's fine for now — filtering them out (stopwords) is a stretch goal if you want an extra challenge.
- Test with both typed input and a file to make sure both paths work.
