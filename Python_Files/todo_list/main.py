# To-Do List Application

# Function to add a task to the list
def add_task(task, tasks):
    tasks.append(task)
    return tasks

# Function to remove a task from the list
def remove_task(task, tasks):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found.")
    return tasks

# Function to display the current tasks
def list_tasks(tasks):
    print("Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Function to save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a file
def load_tasks(filename):
    tasks = []
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file]
    except FileNotFoundError:
        pass
    return tasks

if __name__ == "__main__":
    tasks = load_tasks("tasks.txt")

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks = add_task(task, tasks)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            tasks = remove_task(task, tasks)
        elif choice == "3":
            list_tasks(tasks)
        elif choice == "4":
            save_tasks("tasks.txt", tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
