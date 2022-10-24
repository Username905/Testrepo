#Метод pop() удаляет элемент с указанным его ключом

manufacture = {
    "brand" : "Dodge",
    "model" : "Charger",
    "year" : 2022,
    "color" : "black",
    "colors" : ["red","white"],
    "engine" : 6.2
}

print(manufacture.pop("year"))
print(manufacture)

manufacture.popitem()
print(manufacture)



#Метод copy() создает копию вашего словаря

manufacture.copy()
print(manufacture)

just = {
    "Name" : "Areg",
    "Lastname" : "Shahumyan"
}

print(just)
print(just.copy())