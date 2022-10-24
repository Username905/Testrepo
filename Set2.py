#Метод union() возврашяет новый набор содрежаший все элементы из двух наборов

alph = {"a","b","c"}
numb = {1,2,3}
result = alph.union(numb)
print(result)

#Метод intersection_update() сохраняет те элементы которые присутствуют в обоих наборах

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"apple","gun","knife"}
result = x.intersection(y, z)
print(result)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"apple","gun","knife"}
x.intersection_update(y, z)
print(x)

#Метод symmetric_difference _update() сравнивает два набора 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)