#1

class Conditioner():
    def __init__(self,model,capacity):
        self.model = model
        self.capacity = capacity
    def Turn_On(self):
        print(f"{self.model} is turn on, and in him {self.capacity}")

cond = Conditioner("AAA","15L")

cond.Turn_On()

#2

"""class Animals():
    def __init__(self,animal):
        self.animal = animal
    
    def make_a_sound(self):
        print(f"{self.animal} makes a sound mrrrr")
    def Cat(Animal):
        print(f"")"""

class Animal():
    def make_a_sound(self):
        print("Издает животный звук")
class Cat(Animal):
    def drop_everything(self):
        print("Я все уронил")
class Dog(Animal):
 def dig_the_ground(self):
    print("Я копал из всех сил")

Tom = Cat()
Tom.make_a_sound()
Tom.drop_everything()

#3

class Table():
    def __init__(self,l,w,h):
        self.lenght = l
        self.widht = w
        self.height = h

class DeskTable(Table):
    def square(self):
        return self.widht * self.lenght

t1 = Table(1.5,1.8,0.75)
t2 = DeskTable(0.8,0.6,0.7)
print(t2.square()) #вывод 0.48