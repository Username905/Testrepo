"""Change item value"""

#для изменения элемента списка, можно обратится к индексу

school_subjects = ["Russian", "Mathematics"]
school_subjects[0] = "English"
print(school_subjects)

#изменения диапазона элементов

programming_languages = ["python" , "ruby" , "js" , "go" , "huskell" , "java" , "php"]
programming_languages[3:7] = ["swift" , "cotline" , "C#" , "C++"]
print(programming_languages)

"""Метод append()"""
#метод append() добавляет элемент в конец списка

currensy = ["USD" , "EURO" , "JPY" , "RUR"]
currensy.append("GBP")
print(currensy)

"""метод еxtend()"""

#метод еxtend() расширяет один список другим с конца

cripto_currencies = ["BTC" , "B&B" , "ETH" , "XRP"]
new_cripto_currencies = ["NEO" , "ENG" , "ENJ" , "KSN" ]
cripto_currencies.extend(new_cripto_currencies)
print(cripto_currencies)

latters = ["a","b","c","d"]
numbers = [1,2,3,4]
result = latters + numbers
print(result)

"""метод remove()"""

#метоф remove() удаляет указанный элемент по его названию

capitals = ["Moscow","Erevan","Minsk","Kiev"]
capitals.remove("Moscow")
print(capitals)

"""ключивое слово del"""

#ключивое слово del удаляет элемент по его индексу

countries = ["China","Germany","France","Russia","Belarus"]
del countries[3]
print(countries)

"""метод clear()"""

#метод clear() очишает список, то есть список становится пустим

flowers = ["rose","lily","clove"]
flowers.clear()
print(flowers)

"""метод pop()"""

#метод pop() вырезает элемент по индексу

cars = ["BMW","mercedes","Nissan","Ford","Tesla"]
cars.pop(2)
print(cars)
cars.pop()
print(cars)

