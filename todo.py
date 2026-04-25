import json

# Load tasks
try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except:
    tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})

    elif choice == "2":
        if not tasks:
            print("No tasks")
        else:
            for i, t in enumerate(tasks):
                status = "✔" if t["done"] else "✘"
                print(f"{i+1}. {t['task']} [{status}]")

    elif choice == "3":
        num = int(input("Enter task number: "))
        if 0 < num <= len(tasks):
            tasks[num-1]["done"] = True

    elif choice == "4":
        num = int(input("Enter task number: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)

    elif choice == "5":
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
        print("Saved! Bye 👋")
        break

    else:
        print("Invalid choice")