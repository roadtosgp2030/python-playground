# Python CLI To-Do List — Step-by-Step Guide

## The Plan

Build the app in stages. Each step adds one small piece.

| Step | What you build |
|------|---------------|
| 1 | Print a menu |
| 2 | Get user input |
| 3 | Add a task |
| 4 | View tasks |
| 5 | Delete a task |
| 6 | Loop it |
| 7 | Save to a file |

---

## Step 1: Print a menu

Create a file called `todo.py` in this folder.

Write a **function** called `show_menu` that prints these lines:

```
--- To-Do List ---
1. View tasks
2. Add task
3. Delete task
4. Quit
```

Then **call** that function at the bottom of the file.

Run it with:
```
python todo.py
```

You should see the menu printed in the terminal.

---

## Step 2: Get user input

After calling `show_menu`, ask the user to pick an option.

- Use the built-in `input()` function to read their choice
- Store it in a variable called `choice`
- Print `"You chose: "` followed by what they typed

Run it and make sure it waits for you to type something.

---

## Step 3: Add a task

Before calling `show_menu`, create an **empty list** called `tasks`.

Then write a function called `add_task` that:
- Takes `tasks` as a parameter
- Uses `input()` to ask: `"Enter task: "`
- Appends what the user typed to the `tasks` list
- Prints `"Task added!"`

Call `add_task(tasks)` after the user picks option 2.

---

## Step 4: View tasks

Write a function called `view_tasks` that:
- Takes `tasks` as a parameter
- If the list is **empty**, print `"No tasks yet."`
- Otherwise, loop through the list and print each task with its number

Example output:
```
1. Buy groceries
2. Walk the dog
```

Call `view_tasks(tasks)` after the user picks option 1.

---

## Step 5: Delete a task

Write a function called `delete_task` that:
- Takes `tasks` as a parameter
- Calls `view_tasks(tasks)` to show the current list
- Uses `input()` to ask: `"Enter task number to delete: "`
- Converts the input to an `int`
- Removes the correct task from the list
- Prints `"Task deleted!"`

> Hint: list indexes start at 0, but your display starts at 1.
> So task number 1 is at index 0.

Call `delete_task(tasks)` after the user picks option 3.

---

## Step 6: Loop it

Right now the app runs once and exits. Wrap everything in a **`while True` loop** so it keeps showing the menu.

When the user picks option 4 (Quit):
- Print `"Goodbye!"`
- Use `break` to exit the loop

---

## Step 7: Save to a file

Make tasks persist between runs using a plain text file called `tasks.txt`.

### 7a — Save tasks
Write a function called `save_tasks` that:
- Takes `tasks` as a parameter
- Opens `tasks.txt` in write mode (`"w"`)
- Writes each task on its own line

Call it whenever a task is added or deleted.

### 7b — Load tasks
Write a function called `load_tasks` that:
- Opens `tasks.txt` if it exists (use `os.path.exists`)
- Reads each line and strips the newline character (`\n`)
- Returns a list of tasks
- Returns an empty list if the file doesn't exist

Call it **once** at the start of the program to populate `tasks`.

> Hint: you'll need `import os` at the top of the file.

---

## Tips

- Run your code after every step, not just at the end
- If you get an error, read the last line first — it usually tells you what went wrong
- Ask for help any time you get stuck!
