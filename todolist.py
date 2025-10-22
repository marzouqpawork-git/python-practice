todo=[]
while True:
    print("\n1. Add Task\n2. View Task\n3. Exit")
    choice=input("Enter your choice:  ")
    if choice=='1':
        task=input("Enter task:   ")
        todo.append(task)
        print("Task added successfully")
    elif choice=='2':
        for i,task in enumerate(todo,1):
            print(f"{i}. {task}")
        if todo==[]:
            print("Your todo list is empty")
    elif choice=='3':
        print("Goodbye!!!")
        break
    else:
        print("invalid choice")