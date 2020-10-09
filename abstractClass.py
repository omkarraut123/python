import abc
class My_abc():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_value(self,val):
        pass
    @abc.abstractmethod
    def get_value(self):
        pass
class Myclass(My_abc):
    def set_val(self, input):
        self.val = input

    def get_val(self):
        print("\nCalling the get_val() method")
        print("I'm part of the Abstract Methods defined in My_ABC_Class()")
        return self.val

    def hello(self):
        print("\nCalling the hello() method")
        print("I'm *not* part of the Abstract Methods defined in My_ABC_Class()")      
my_class = Myclass()

my_class.set_val(10)
print(my_class.get_val())
my_class.hello()