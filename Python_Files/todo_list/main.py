# To-Do List Application

# Function to add a task to the list
def add_task(task, tasks):
    tasks.append(task)  # Add the new task to the tasks list
    return tasks

# Function to remove a task from the list
def remove_task(task, tasks):
    if task in tasks:  # Check if the task exists in the list
        tasks.remove(task)  # Remove the task if it exists
    else:
        print("Task not found.")  # Print an error message if the task is not found
    return tasks

# Function to display the current tasks
def list_tasks(tasks):
    print("Your To-Do List:")  # Print a header for the list
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")  # Print each task with a number

# Function to save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, "w") as file:  # Open the file in write mode
        for task in tasks:
            file.write(task + "\n")  # Write each task to the file

# Function to load tasks from a file
def load_tasks(filename):
    tasks = []
    try:
        with open(filename, "r") as file:  # Open the file in read mode
            tasks = [line.strip() for line in file]  # Read and store each line as a task
    except FileNotFoundError:
        pass  # Ignore if the file is not found
    return tasks

if __name__ == "__main__":
    tasks = load_tasks("tasks.txt")  # Load tasks from the file

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")  # Get the user's choice

        if choice == "1":
            task = input("Enter a task: ")  # Prompt the user for a task and add it
            tasks = add_task(task, tasks)
        elif choice == "2":
            task = input("Enter the task to remove: ")  # Prompt the user for a task to remove
            tasks = remove_task(task, tasks)  # Remove the task
        elif choice == "3":
            list_tasks(tasks)  # List all the tasks
        elif choice == "4":
            save_tasks("tasks.txt", tasks)  # Save the tasks to the file
            print("Goodbye!")
            break  # Exit the loop and the program
        else:
            print("Invalid choice. Please select a valid option.")  # Handle invalid choices
