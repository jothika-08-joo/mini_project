tasks=[]
while True:
    print("MENU")
    print("1.Add tasks")
    print("2.Show tasks")
    print("3.Remove tasks")
    print("4.Exit")
    a=input("enter the number of menu:")
    if a=="4":
        break
    elif a=="1":
        b=int(input("enter your number of tasks"))
        for i in range(b):
            user_task=input("enter your task:")
            tasks.append(user_task)
        print("your tasks are added successfully")      
    elif a=="2":
        if tasks!=[]:
            print("your tasks are:")
            for i in range(len(tasks)):
                print(f"  ",i+1,".",tasks[i])     
        else:
            print("you have  to add the task first choose no.1 to add task")        
    elif a=="3":
        num=int(input("enter a no.of tasks to remove:"))
        for i in range(num):
            remove_task=input("enter name of your finished task: ")    
            tasks.remove(remove_task)
        print("tasks are removed")    


