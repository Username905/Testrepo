"""коллекции в пайтон"""

"""коллекции в пайтон это, некие контейнерные типы данных"""



"""LIST(список)"""
this_list = ["a","b","c", 1, 2 , 3 , 4.0 , 5.0 , 6.0 , True , False]
print(this_list)
print(type(this_list))
print(len(this_list))

#list(список) - исползуется для хранения множества эелементов различних типов в одной переменной с помощю []

"""Элементы списка упорядечены, изменяемы, дублеруемы, многотипичны"""

#элементы списка индексируются первый элемент имеет индекс 0

"""упорядеченный список имеет определенный порядок"""

#при добовлении элемента он будет помещен в конец, но используя методы данного списка элемент может помещен в любое место

#список можно изменять, то есть добовлять, заменять, удалять, изменять типы этого списка

#в данном списке разрешены хранить одинаковые значения



"""TUPLE(кортеж)"""
this_tuple = ("a","b","c", 1, 2 , 3 , 4.0 , 5.0 , 6.0 , True , False)
print(this_tuple)
print(type(this_tuple))
print(len(this_tuple))

#tuple(кортеж) - исползуется для хранения множества эелементов различних типов в одной переменной с помощю ()

#tuple это упорядеченная но изменяемая коллекция, дублеруемая

"""DICTIONARY(словарь)"""
this_dict = {
    "brand" : "BMW", 
    "model" : "X6M", 
    "color" : "grey",
    "engine" : 4.4 , 
    "price" : 150000
}
print(this_dict)
print(type(this_dict))
print(len(this_dict))

#используется для хранения множества данных в парах - ключь(key) значения(value)

#словарь упорядочен, изменяем, его ключи не могут повторятся а значения могут

#солварь определяется {} и хранит данные в паре ключь и значения  

"""SET(набор)"""
this_set = {"BMW" , "BMW" , 635 , 635 , 4.4 , 4.4}
print(this_set)
print(type(this_set))
print(len(this_set))
#набор исползуется для хранения множества эелементов различних типов в одной переменной с помощю {}

#набор является не упорядоченным, не индексированным, не имеет дубликатов
