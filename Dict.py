"""Словарь используется для хранения данных в парах ключ : значение(словарь упорядоченный,изменяемый но не допускаюший дубликат)"""


manufacture = {
    "brand" : "Dodge",
    "model" : "Charger",
    "year" : 2022,
    "color" : "black",
    "colors" : ["red","white"],
    "engine" : 6.2
}

print(manufacture["brand"])
print(manufacture)
print(type(manufacture))
print(len(manufacture))


#Метод get() дает возможность получить значения по его ключу

print(manufacture.get("color"))

#Метод keys() возврашяет все ключи словаря

just_dict = {
    "brand" : "BMW",
    "model" : "M5"
}

just_dict.keys()
print(just_dict.keys())

manufacture["hp"] = 700
print(manufacture)

#Метод values() возврашяет все значение словаря

manufacture.values()
print(manufacture.values())

manufacture["year"] = 2015
print(manufacture)

#Метод items() возврашяет каждый элемент словаря в виге кортежей

manufacture.items()
print(manufacture.items())

manufacture.update({"NM" : 850})
print(manufacture)

