#Аргумент по умолчанию

"""1.Аргументам функции в питон можно присваивать значения по умолчанию, используя оператор присвоения(=)"""

"""Аргумент по умолчанию"""

def greet(name, msg="Hello"):
    """Эта функция выводит для человека с именем name сообщение message. Если текст сообщения не передан, по умолчанию используется "Доброе утро"!"""
    print("Hello,", name + ", " + msg)

greet("Areg")
greet("Мария", "как твои дела")

#Именнованный аргумент

"""Когда мы вызиваем функциэ с значениями, эти значения присвоиваются аргументам в соответствии с их позицей"""

#2 именованных аргумента greet(name = "Mika", msg = "Как дела?")
#2 
