"Метод инит это специальный метод который автоматический выполняется при создании каждого нового экземпляра на базе класса"
"Селф это ссылка на экз. которое предоставляет конкретному экземпляру доступ к атрибутам и методам класса"

class Dog():
    """Простая модель собаки"""

    def __init__(self,name,age):
        """Инициализурует атрибуты name и age"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(f"{self.name} is now siting")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.name} roll over")

Aregs_dog = Dog("Chappi", 5)

print(Aregs_dog.name)
print(Aregs_dog.sit())
Aregs_dog.roll_over()

print(f"My dogs name is {Aregs_dog.name}")
print(f"My dog is {Aregs_dog.age} years old")