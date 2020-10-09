class MyClass(object):

    def func(self,a):
        print("I'm being called from the Parent class",a)


class ChildClass(MyClass):

    def func(self):
        print("I'm actually being called from the Child class")
        print("But...")
        # Calling the `func()` method from the Parent class.
        super(ChildClass, self).func(20)

my_instance_2 = ChildClass()
my_instance_2.func()
