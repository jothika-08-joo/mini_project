import random
print("you have only 10 chances!,guess the number 1 to 100")
b=random.randint(1,100)
found=False

for i in range(10):
    try:
      a=int(input("guess a num:"))
      if a<0 or a>100:
        print("enter a number between 1 to 100")
        continue 
      if a==b:
        print("you found it 🥳🥳!!!!!")
        found=True
        break
      elif a<b:
        print("too low")
        print(f"😢you have only",(10-(i+1)),"chance")
      elif a>b:
        print("too high")
        print(f"😢you have only",(10-(i+1)),"chance")
    except:
        print("enter a valid numbers 1 to 100")  
if found==False:
    print(f"😢the game is over ,the number was",b)     
        

    
    

        
    