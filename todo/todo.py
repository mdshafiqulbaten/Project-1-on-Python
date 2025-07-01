tasks = []

def show_menu():
    print("\nTo-Do List:")
    print("1. Add task\n2. Remove task\n3. View tasks\n4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
    elif choice == '2':
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        idx = int(input("Enter task number to remove: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
    elif choice == '3':
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == '4':
        break
    else:
        print("Invalid choice!")
