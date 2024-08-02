"""
    To Do List 
    - Add task
    - View task
    - Delete task
    - Quit
"""

tasks = []


#   Function Add Task
def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added successfully!")


#   Function View Task
def view_tasks():
    if len(tasks) == 0:
        print("\nList of tasks: ")
        print("No tasks in here.")
    else:
        print("\nList of tasks: ")
        for pos, task in enumerate(tasks):
            print(f"{pos + 1}. {task}")


#   Function Add Task
def delete_task():
    if len(tasks) == 0:
        view_tasks()
        print("\nYou must be choice 1 to add task!")
    else:
        view_tasks()
        try:
            choiceTask = int(input("\nEnter your task number to delete: "))

            if 0 < choiceTask <= len(tasks):
                del tasks[choiceTask - 1]
                print("Task deleted successfully!")
            else:
                print("Your choice is not have in list of tasks!")
        except ValueError:
            print("Invalid input. Please enter an integer.")


#   Function Main App
def main():
    while True:

        print("\n========== To Do List Application ==========")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4. Quit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("\nThank you for using the To Do List Application!")
                break
            else:
                print("\nInvalid your choice! Please try again.")

        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
