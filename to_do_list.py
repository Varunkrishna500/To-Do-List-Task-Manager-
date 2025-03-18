class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\n=== To-Do List ===")
        for index, task in enumerate(self.tasks, start=1):
            status = "✔️ Completed" if task["completed"] else "❌ Not Completed"
            print(f"{index}. {task['task']} - {status}")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task description: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            task_number = int(input("Enter task number to mark as completed: "))
            todo.mark_completed(task_number)
        elif choice == "4":
            todo.view_tasks()
            task_number = int(input("Enter task number to delete: "))
            todo.delete_task(task_number)
        elif choice == "5":
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
