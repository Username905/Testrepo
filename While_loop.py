#The While loop

"""С помощю цикла While мы можем выполнять перебор элементов, до тех пор пока условия истина"""

item = 3

while item < 10:
    print(item)
    item += 1

#The break statements

"""С помощю оп. break мы можем остановить цикл даже если условия истина"""

num  = 1

"""while num < 12:
    print(num)
    num += 1"""

while num < 12:
    print(num)
    if num == 4:
     break
    num += 1

#The continues statement

"""С по0мощю оп. continue мы можем остановить текущую ипер"""

i = 0

while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#The else Statement

"""Оп. else срабатывает когда условие больше не выполняется"""

num3 =2

while num3 < 20:
    print(num3)
    num3 += 1
else:
    print("num3 is no longer less than 20")

#Tasks

Text = "Variable"
Cond = 0

while Cond < len(Text):
    print(Text[Cond])
    Cond += 1 


"""n = 200

while n == 200:  #an infinite loop
    data = input("Enter something: ")
    print("You entered : ", data)
print("Good Bye my Friend!")"""

total = 150

while total > 0:
    n = int(input("Enter your num: "))
    total == total - n
print("Resurse finished")