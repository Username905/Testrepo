"""#1

Запрашываем целое число у пользователя

number = int(input("Enter some number: "))

# useing operators modulus (%)

if (number % 2 == 1):
    print("Нечетное")
else:
    print("Четное")"""

"""#2

Угадайте фигуру

num = int(input("Enter some number: "))

if num == 3:
    print("Триугольник")
elif num == 4:
    print("Прямоугольник")
elif num == 5:
    print("Пятиугольник")
elif num == 6:
    print("Шестигольник")
elif num == 7:
    print("Семиугольник")
elif num == 8:
    print("Восьмигольник")
elif num == 9:
    print("Девятиугольник")
elif num == 10:
    print("Десятиугольник")
#Выводим ошибку ввода
if num == " ":
 print("Введенное количество сторон не поддерживается программой.")
else:
 print("Эта фигура:", num)"""

"""# Запрашиваем у пользователя количество сторон 
nsides = int(input("Введите количество сторон фигуры: ")) 
# Определяем вид фигуры, оставляя его пустым, если введено некорректное число 
name = "" 
if nsides == 3: 
 name = "треугольник" 
elif nsides == 4: 
 name = "прямоугольник" 
elif nsides == 5: 
 name = "пятиугольник" 
elif nsides == 6: 
 name = "шестиугольник" 
elif nsides == 7: 
 name = "семиугольник" 
elif nsides == 8: 
 name = "восьмиугольник" 
elif nsides == 9: 
 name = "девятиугольник" 
elif nsides == 10: 
 name = "десятиугольник" 
# Выводим ошибку ввода 
if name == "": 
 print("Введенное количество сторон не поддерживается программой.") 
else: 
 print("Эта фигура:", name)"""

"""Сколько дней в месяце

month = input("Enter month: ")

if month == "January":
    print(31)
elif month == "February":
    print(28)
elif month == "March":
    print(31)
elif month == "April":
    print(30)
elif month == "May":
    print(31)
elif month == "June":
    print(30)
elif month == "July":
    print(31)
elif month == "August":
    print(31)
elif month == "September":
    print(30)
elif month == "October":
    print(31)
elif month == "November":
    print(30)
elif month == "December":
    print(31)
else:
    print("Error")"""

"""#Запрашиваем у пользователя название месяца 
month = input("Введите название месяца: ") 
# Вычисляем количество дней в месяце 
days = 31  
if month == "Апрель" or month == "Июнь" or \ 
 month == "Сентябрь" or month == "Ноябрь": 
 days = 30
elif month == "Февраль": 
 days = "28 or 29"  
# Выводим результат 
print("Количество дней в месяце", month, "равно", days)"""

#Запрашиваем у пользователя дату(месяц и день) 

month = input("Enter name month: ")
day = int(input("Enter day: "))

#Определяем сезон

if month == "January" or "February":
    print("Winter")
elif month == "March":
    if day <= 20:
        print("Winter")
    else:
        print("Spring")
elif month == "April" or month == "May":
    print("Spring")
elif month == "June":
    if day <= 21:
        print("Spring")
    else:
        print("Summer")
elif month == "July" or month == "August":
    print("Summer")
elif month == "September":
    if day <= 21:
        print("Summer")
    else:
        print("Autumn")
elif month == "October" or "November":
    print("Autumn")
elif month == "December":
    if day <= 21:
        print("Autumn")
    else:
        print("Winter")