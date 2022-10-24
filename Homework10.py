#1

class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} it has five stars of Michelin")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opens at 9:00 o'clock")

restaurant = Restaurant("У Ашотика", "Japanse")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#2

class User():

    def __init__(self,frist_name,last_name,age,city):
        self.frist_name = frist_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"Me {self.frist_name} {self.last_name}, i am {self.age}, I live in {self.city}")
    
    def greet_user(self):
        print(f"Hi, my name is {self.frist_name} {self.last_name}, i'm {self.age} years old, I live in {self.city}")

user1 = User("Areg","Shahumyan",17,"Kvartal")
user2 = User("Tigran","Adamyan",17,"Yerevan")
user3 = User("Grisha","Sargsyan",19,"Kvartal tex")

print(user1.frist_name)
print(user1.last_name)
print(user1.age)
print(user1.city)
user1.describe_user()
user1.greet_user()

print(user2.frist_name)
print(user2.last_name)
print(user2.age)
print(user2.city)
user2.describe_user()
user2.greet_user()

print(user3.frist_name)
print(user3.last_name)
print(user3.age)
print(user3.city)
user3.describe_user()
user3.greet_user()