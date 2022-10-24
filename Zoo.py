"""Baby = 2 #0
Junior = 12 #14
Human = 64 #23
Older = 65 #18

num = list(map(int,input("\nEnter the numbers : ").split(',')))

while num != "":
    if num <= Baby:
        baby_ticket = 0
    elif num <= Junior:
        junior_ticket = 14
    elif num <= Human:
        human_ticket = 23
    elif num >= Older:
        older_ticket = 18
    else:
        print("Error")
    num =+ 1

print(num)"""

#Стоимость билетов по возростным категориям

baby_price = 0.00
child_price = 12.00
adult_price = 18.00
senior_price = 15.00

#Возрастные ограничения по категориям

baby_limit = 2
child_limit = 12
adult_limit = 64

#Общая сумма посещения

total = 0

# Ввод возраста посетителя 

peoples = input("Введите возраст посетителя (пустая строка для окончания ввода): ")

#Не может быть пустым
while peoples != "":
    age = int(peoples)

#Добавление стоимости билеты к общей сумме

    if age <= baby_limit:
        total = total + baby_price
    elif age <= child_limit:
        total = total + child_price
    elif age <= adult_limit:
        total = total + adult_price
    else:
        total = total = senior_price

    #Возраст следующего посетителя
    peoples = input("Введите возраст посетителя (пустая строка для окончания ввода): ")

#Сумма всех посетителей
print("Общая сумма посетителей составляет $%.2f" % total)