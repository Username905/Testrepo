"""feet = int(input("Enter feet: "))

inches = int(input("Enter inches: "))

sm = feet * 12

sm1 = inches * 2.54

print(sm)
print(sm1)"""

ft = 12
inch = 2.54

print("Введите ваш рост:  ")

#ВВод данных пользователя

feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

sm = (feet * ft + inches) * inch

#Отображение результата
print("Ваш рост составляет в см:  ", sm)