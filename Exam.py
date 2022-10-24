n1 = int(input("Введите целое число: "))
n2 = 0
 
while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit  
 
print('"Обратное" ему число:', n2)

n = int(input('Факториал: '))

factorial = 1

for i in range(2, n+1) :
    factorial *= i
print(factorial)


fib1 = fib2 = 1

n = int(input("Фибоначчи: "))

print(fib1, fib2, end=' ')

for i in range(2, n) :
    fib1, fib2 = fib2, fib1 + fib2
print(fib2, end='\n')

x = {10, 20, 30, 40, 50, 60}
y = {40, 50, 90}
z = {40, 90, 100}
x.intersection_update(y, z)
print(x) 

just_list = [10,11,12,30,62,54,845,15,20,11,20,36]

if len(set(just_list)) == len(just_list) :
    print("Все элементы уникальны")
else :
    print("есть совпадения")