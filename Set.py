"""Set используется для хранения элементов разных типов"""

#Set создается с помощю {}


this_set = {"Vahagn","Armine","Tamara","Areg"}
print(this_set)
print(type(this_set))
print(len(this_set))

#Метод add()

#Метод add() добавляет элемент в конец нашего списка но мы это не заметим

colors = {"yellow","blue","green"}
colors.add("black")
print(colors)
print(type(colors))
print(len(colors))

#Метод update() аналод extande
#Метод update() расширяет один список другим списком добавляя его в конец но так как список не упорядоченный мы это не заметим
#Можно добавить другой список

new_colors = {"white","orange"}
colors.update(new_colors)
print(colors)
print(type(colors))
print(len(colors))

my_favorit_colors = ("asd","assd")
colors.update(my_favorit_colors)
print(colors)

#Метод remove() удаляет элемент

colors.remove("asd")
print(colors)

#Метод discard()
#если удаляемый элемент не существует в SET метод remove() выдаст ошибку 

"""Метод discard() удаляет элемент если элемента не существует ошубки не будет"""

colors.discard("assd")
print(colors)

#Метод clear() очишает элементы

just_set = {"A","B","C","D"}
just_set.clear()
print(just_set)

just_set1 = {"ABC","DEF"}
del just_set1

"""Вы также можете использовать метод pop() для удаления элемента, но этот метод удалит последний элемент. Помните, что наборы неупорядочены, поэтому вы не будете знать, какой элемент будет удален. Возвращаемое значение метода pop() — удаленный элемент."""

"""Примечание. Наборы неупорядочены, поэтому при использовании метода pop() вы не знаете, какой элемент удаляется."""

"""Удаляет последний элемент с помощью метода pop()."""

"""Метод pop вырезает эл. по индексу"""

just_set2 = {"Dollar","Euro","RUR"}
just_set3 = list(just_set2)
just_set3.pop(2)
just_set3 = set(just_set2)
print(just_set2)

#printhisset = {"apple", "banana", "cherry"}
#x = thisset.pop()

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()