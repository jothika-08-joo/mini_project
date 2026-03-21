print("1.Add task")
print("2.finished task")
a=int(input("enter 1 or 2: "))
add_task=[]
if a==1:
    num=int(input("enter a number of tasks:"))
   
    for i in range(num):
        task=input("task:")
        add_task.append(task)
    print("tasks were added🥳") 
    print("your tasks are:")   
for i in range(len(add_task)):
    print(i+1,".",add_task[i])  

if a==2:
    for i in range(len(add_task)):
       print(i+1,".",add_task[i])  
    fin=int(input("enter your finished task number:"))   
    add_task.pop(fin-1)
    print("your remaining tasks are:")
    for i in range(len(add_task)):
        print(i+1,".",add_task[i])  




    