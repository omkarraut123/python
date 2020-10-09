class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{0} eats {1}'.format(self.name, food))


class Dog(Animal):

    def fetch(self, thing):
        print('{0} goes after the {1}!'.format(self.name, thing))

    def show_affection(self):
        print('{0} wags tail'.format(self.name))


class Cat(Animal):

    def swatstring(self):
        print('{0} shreds more string'.format(self.name))

    def show_affection(self):
        print('{0} purrs'.format(self.name))

for a in (Dog('Rover'), Cat('Fluffy'), Cat('Lucky'), Dog('Scout')):
    a.show_affection()