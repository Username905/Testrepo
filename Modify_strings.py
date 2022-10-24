"""В пайтон есть методы которые дают работать с регистрами строк"""
#Метод upper()возвращает строку в верхнем регистре

sevenup = "juice" 
print(sevenup.upper())
#Метод lower()опускает строку на нижный регистр
load = "DOWNLOAD"
print(load.lower())

#strip
#Метод strip удаляет пробелы в нашей сроке

universry = "          happy        couch"
print(universry.strip())

#Replace Strin(заменить элемент строки)

prog = "i am programmer"
print(prog.replace("p", "t"))

"""Strin concatenation"""

freedom = "my"

quality = "life" 

result = freedom + quality
result1 = freedom + " " + quality
print(result)
print(result1)