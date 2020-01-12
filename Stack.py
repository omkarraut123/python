class Stack:

    def __init__(self):
        self.stack=[]

    def is_empty(self):
        if(len(self.stack)==0):
                return 1
        else:
            return 0          

    def push(self,value):
        self.stack.append(value)   

    def pop(self):
        return self.stack.pop()    

s=Stack()
while(True):
    print("Enter your choice....")
    print("1.push\n2.pop\n3.quit")
    choice=int(input())
    if choice==1:
        value=int(input("Enter value for push in stack : "))
        s.push(value)
 
    elif choice==2:
        if(s.is_empty()):
            print("stack is empty")
        else: 
            print("pop element is ",s.pop())

    elif choice==3: 
        print("good bye..")
        break   
    
