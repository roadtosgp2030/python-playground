def show_menu():
    print(
        """--- To-Do List ---
1. View tasks
2. Add task
3. Delete task
4. Quit"""
    )

    tasks = []
    try:
        with open("tasks.txt", "r") as f:
            tasks = [line.strip() for line in f]
    except FileNotFoundError:
        tasks = []

    while True:
        option = int(input("Pick an option: "))
        print(f"You chose: {option}")

        match option:
            case 1:
                view_tasks(tasks)
            case 2:
                add_task(tasks)
            case 3:
                delete_task(tasks)
            case 4:
                print("Good bye")
                break
            case _:
                print("Options not exists")


def add_task(tasks):
    task = input("Enter task: ")
    with open("tasks.txt", "a") as f:
        f.write(f"{task}\n")
    tasks.append(task)
    print("Task added!")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")


def delete_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return
    task_num = int(input("Enter task number to delete: "))
    if task_num <= len(tasks):
        tasks.pop(task_num - 1)
    else:
        print("Task number not exist.")
        return
    with open("tasks.txt", "w") as f:
        f.write("\n".join(tasks) + "\n")
    print("Task deleted!")


show_menu()
