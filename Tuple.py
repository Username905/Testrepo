"""Tuple используется для хранения элементов различного типа"""

"""Элементы кортежа упорядечены, не изменяемы, допускают дублирование, кортеж создается с помощю ()"""


vegetables = ("tomato","cucumber","beetroot")

#создание кортежа с одним элементом

streets = ("Mashtots str",)
print(type(streets))

#Note tuple

market = ("Krpak")
print(type(market))

#Диапазон индексов

fruits = ("cherry","banana","apple","pinaplle","melon","watermelon","peach","dragon fruit")
print(fruits[:6])
print(fruits[2:])
print(fruits[-7:-3])

#Change tuple valuts(изменение значения кортежа с лист)

cars = ("Ford","Tesla","Lincoln","GMC")
new_cars = list(cars)
new_cars.append("Cadillac")
print(new_cars)
cars = tuple(new_cars)
print(type(cars))
print(cars)

just_tuple = ("Earth","Mars","Mercury","Pluton","Venera")
just_tuple1 = list(just_tuple)
just_tuple1.append("Sun")
print(just_tuple1)
just_tuple = tuple(just_tuple1)
print(type(just_tuple))
print(just_tuple)

#Add tuple to tuple(добавить кортеж в кортеж)

asian_country = ("China","Japan","South Korea","North Korea")
europian_countrys = ("Germany",)
asian_country += europian_countrys
print(asian_country)
print(type(asian_country))

rappers = ("Tupac","Notoriuos BIG","Eminem","Miyagi")
rap = list(rappers)
del rap[2]
print(rap)
rappers = tuple(rap)
print(rappers)
print(len(rappers))
print(type(rappers))

just = ("BMW","Porsche","Tesla","Mercedes")
(black,white,red,yellow) = just
print(just)
print(black)
print(white)
print(red)
print(yellow)

number = ("QWE","RTY","WASD")
(WASD,RTY,QWE) = number
print(number)
print(WASD)
print(RTY)
print(QWE)

apples_phone = ("X","11","11 pro max","12","12 pro max","13")
print(apples_phone)
(black,white,*red) = apples_phone
print(apples_phone)
print(black)
print(white)
print(red)

alphabet = ("a","b","c","d","e","f","g","h","i","j")
(Pink,blue,*green) = alphabet
print(alphabet)
print(Pink)
print(blue)
print(green)