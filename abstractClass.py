from abc import ABC, abstractmethod
 
 
class AbstractClass(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()
 
    @abstractmethod
    def eat(self):
        pass
 
 
class Parents(AbstractClass):
    def eat(self):
        return "Eat solid food " + str(self.value) + " times each day."
 
 
class Babies(AbstractClass):
    def eat(self):
        return "Milk only " + str(self.value) + " times or more each day."
 
 
food = 3
adult = Parents(food)
print('Adult')
print(adult.eat())
 
infant = Babies(food)
print('Infants')
print(infant.eat())
 