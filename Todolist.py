Tasks = []

while True:
    print("\n==== TO-Do lIST ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delet Task")
    print("4. Exit")

    Choice = input("Enter your choice between 1-4: ")

    if Choice == 1:
        Task = input("Enter a task: ")
        Tasks.append[Task]
        print("Task added successfully")
    elif Choice == 2:
        if len(Tasks) == 0:
            print("No task avalable")
        else:
            print("\ntasks: ")
            for i, Task in enumerate(Tasks, start=1):
                print(f"{i}. {Task}")




