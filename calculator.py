
class cal:
    def __init__(self):
        self.a=int(input("enter a number:"))
        self.b=int(input("enter a number:"))
        self.c=input("enter a operator add/sub/mul/div:")
        if self.c == "add":
            print(self.add())
        elif self.c=="sub":
            print(self.sub())
        elif self.c=="mul":
            print(self.mul())
        elif self.c=="div":
            print(self.div())        
   

    def add(self):
        c=self.a+self.b
        return c  
    

    def sub(self):
        c=self.a-self.b
        return c  
   

    def mul(self):
        c=self.a*self.b
        return c  
    

    def div(self):
        c=self.a/self.b
        return c  
joo=cal()



'''
#without using functions
a=float(input("enter a num:"))
b=float(input("enter a num:"))
operator=input("choose operator +,-,*,/:")

if operator=="+":
    result=a+b
    print (result)
elif operator=="-":
    result = a-b
    print (result)

elif operator=="*":
    result = a*b
    print (result)
elif operator=="/":
    result = a/b
    print (result)  
else:
    print("enter valid operator")      
'''
