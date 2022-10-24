class Bicycle():
    """Тип задачи велосипед"""

    def __init__(self,brand,color,type):
        self.brand = brand
        self.color = color
        self.type = type

    def drive(self):
        print(f"{self.brand}'s {self.color}, {self.type} bike rides well")

    def brakes(self):
        print(f"{self.brand}'s {self.color}, {self.type} bike brakes well")

    def allin_one(self):

        full_name = f"{self.brand} {self.color} {self.type}"
        return full_name.title()

bike = Bicycle("Rambo","Black","Sport")

print(bike.brand)
print(bike.color)
print(bike.type)
print(bike.allin_one())
bike.drive()
bike.brakes()