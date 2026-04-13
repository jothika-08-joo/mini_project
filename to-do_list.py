tasks=[]
def add_tasks():
    try:
        b=int(input("enter your number of tasks:"))
        for i in range(b):
            user_task=input("enter your task:")
            tasks.append(user_task)
        print("your tasks are added successfully")   
    except:
        print("enter a valid number") 
def show_tasks():
    if tasks!=[]:
        print("your tasks are:")
        for i in range(len(tasks)):
            print(f"  ",i,".",tasks[i])     
    else:
        print("you have  to add the task first choose no.1 to add task")  
def remove_tasks():
    show_tasks()
    try:
        num=int(input("enter a number of your task to remove:"))
        if 0<=num<=len(tasks)-1:
                tasks.pop(num)
                print("tasks are removed")
        else:
            print("enter a valid number of task")        
    except:
        print("enter a valid number")    
def update_tasks():
    show_tasks()
    try:    
        update_num=int(input("enter the task number to update:"))
        if 0<=update_num<=len(tasks)-1:
            update_task=input("enter your new task name:")
            tasks[update_num]=update_task
            print("updated successfully")
        else:
            print("enter a correct task number")
    except:
        print("enter a valid number")    


while True:
    print("MENU")
    print("1.Add tasks")
    print("2.Show tasks")
    print("3.Remove tasks")
    print("4.Update tasks")
    print("5.Exit")
    a=input("enter the number of menu:")
    

    if a=="5":
        break

    elif a=="1":
        add_tasks()
             
    elif a=="2":
        show_tasks()
              
    elif a=="3":
        remove_tasks()

    elif a=="4":
        update_tasks()
        

