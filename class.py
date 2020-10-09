class Myclass:
    value=10
    count=0
    def __init__(self,val):
        self.val=self.filterint(val)
        Myclass.count+=1
    @staticmethod
    def filterint(value):
        if not isinstance(value,int): 
            print("Enter value is not an INT,value set to 0")   
            return 0
        else:
            return value    
    def set(self,val):
        self.v=val
        self.get()
    def get(self):
        print(self.v)            

          
ob=Myclass(5) 

#ob1=Myclass(10)
#ob2=Myclass(15)
#print(ob.count)
#print(ob1.count)
#print(ob2.count)
#print(ob.filterint(100))
ob.set(10)

#ob.get() 