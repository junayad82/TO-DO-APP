tasks = []

while True:

    print("\n===== TODO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Show Completed Tasks")
    print("7. Show Pending Tasks")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":

        task_name = input("Enter task: ")

        task = {
            "name": task_name,
            "completed": False
        }

        tasks.append(task)

        with open("tasks.txt", "a") as file:
            file.write(f"{task_name} | Pending\n")

        print("Task added successfully!")

    # View Tasks
    elif choice == "2":

        if len(tasks) == 0:
            print("No task available")

        else:
            print("\nTask List:")

            for i, task in enumerate(tasks, start=1):

                status = "✅" if task["completed"] else "❌"

                print(f"{i}. {task['name']} {status}")

    # Search Task
    elif choice == "3":

        search_task = input("Enter task name: ")

        found = False

        for task in tasks:

            if search_task.lower() == task["name"].lower():

                status = "Completed" if task["completed"] else "Pending"

                print(f"{task['name']} - {status}")

                found = True
                break

        if not found:
            print("No task found")

    # Complete Task
    elif choice == "4":

        complete_task = input("Enter task name: ")

        found = False

        for task in tasks:

            if complete_task.lower() == task["name"].lower():

                task["completed"] = True

                print("Task completed!")

                found = True
                break

        if not found:
            print("No task found")

    # Delete Task
    elif choice == "5":

        delete_task = input("Enter task name: ")

        found = False

        for task in tasks:

            if delete_task.lower() == task["name"].lower():

                tasks.remove(task)

                print("Task deleted!")

                found = True
                break

        if not found:
            print("No task found")

    # Show Completed Tasks
    elif choice == "6":

        print("\nCompleted Tasks:")

        found = False

        for task in tasks:

            if task["completed"]:

                print(task["name"])

                found = True

        if not found:
            print("No completed tasks")

    # Show Pending Tasks
    elif choice == "7":

        print("\nPending Tasks:")

        found = False

        for task in tasks:

            if not task["completed"]:

                print(task["name"])

                found = True

        if not found:
            print("No pending tasks")

    # Exit
    elif choice == "8":

        print("Goodbye!")

        break

    else:
        print("Invalid choice")