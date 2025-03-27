
todo_list = []


def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")


def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(todo_list, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{index}. {task['task']} [{status}]")


def add_task():
    task_name = input("Enter the task: ")
    todo_list.append({'task': task_name, 'completed': False})
    print(f"Task '{task_name}' added!")
def mark_task_completed():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(todo_list):
            todo_list[task_number]['completed'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def remove_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_number < len(todo_list):
            removed_task = todo_list.pop(task_number)
            print(f"Task '{removed_task['task']}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
while True:
    display_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select again.")
