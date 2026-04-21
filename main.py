import json

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

tasks = load_tasks()

def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Completed Tasks")
    print("4. View Pending Tasks")
    print("5. Delete Task")
    print("6. Mark Task Completed")
    print("7. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    # ADD TASK
    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print("✅ Task added!")

    # VIEW ALL TASKS
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nAll Tasks:")
            for i, t in enumerate(tasks):
                status = "✔" if t["done"] else "❌"
                print(f"{i+1}. {t['task']} [{status}]")

    # VIEW COMPLETED TASKS
    elif choice == "3":
        completed = [t for t in tasks if t["done"]]
        if not completed:
            print("No completed tasks.")
        else:
            print("\nCompleted Tasks:")
            for i, t in enumerate(completed):
                print(f"{i+1}. {t['task']} ✔")

    # VIEW PENDING TASKS
    elif choice == "4":
        pending = [t for t in tasks if not t["done"]]
        if not pending:
            print("No pending tasks.")
        else:
            print("\nPending Tasks:")
            for i, t in enumerate(pending):
                print(f"{i+1}. {t['task']} ❌")

    # DELETE TASK
    elif choice == "5":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t['task']}")
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"🗑 Removed: {removed['task']}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("⚠️ Enter a valid number!")

    # MARK TASK COMPLETED
    elif choice == "6":
        if not tasks:
            print("No tasks available.")
        else:
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t['task']}")
            try:
                num = int(input("Enter task number to mark complete: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["done"] = True
                    save_tasks(tasks)
                    print("✔ Task marked as completed!")
                else:
                    print("Invalid number.")
            except ValueError:
                print("⚠️ Enter a valid number!")

    # EXIT
    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")