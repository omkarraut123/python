class address:
    def __init__(self,pin_no,city):
        self.pin_no=pin_no
        self.city=city
        

class person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def details(self):
        print(self.name," ",self.age)    
        print(self.address.pin_no," ",self.address.city)

    def update(self,addr):
        self.address=addr

add1=address(1001,"pune")
add2=address(1002,"banglore")
p1=person("omkar",21,add1)
p2=person("nileh",22,add2)
p1.details()
p2.details()


