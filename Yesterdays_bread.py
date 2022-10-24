# Вычисляем стоимость вчерашнего хлеба

# Стоимость свежого хлеба

bread_price = 2.55

# Скидка на старый хлеб 

discount_rate = 0.42

#Запрашываем данные у пользователя

num_loves = int(input("Укажите кол-во вчерашнего хлеба: "))

# Вычисляем общюю стоимость и скидку

regular_price = num_loves * bread_price

discount = regular_price * discount_rate

result = regular_price - discount

#Отображение результата в нужном формате

print("Номинальная цена: %5.2f" % regular_price)
print("Сумма скидки: %5.1f" % discount)
print("Итого: %5.1f" % result)