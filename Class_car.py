class Car():
    """Простая модель машины"""

    def __init__(self,make,model,year):
        """Инициализирует произвотство автомобиля"""
        self.make = make
        self.model = model
        self.year = year

    def descriptis_name(self):
        """Акуратно отформатирование автомобиля"""
        full_name = f"{self.make} {self.model} {self.year}"
        return full_name.title()

my_car = Car("BMW","M5",2020)

print(my_car.descriptis_name())