#1

def seasons(month):
    
    if month == 12 or 1 <= month <= 2:
        print("Winter")
    elif 3 <= month <= 5:
        print("Spring")
    elif 6 <= month <= 8:
        print("Summer")
    elif 9 <= month <= 11:
        print("Autumn")
    else:
        print("Неверное число, попробуйте ещё")

num = int(input("Введите число: "))

seasons(num)

#2

#3

word = input("Введите слово: ")
if str(word) == str(word)[::-1] :
    print("Is a Palindrome")
else:
    print("Is not a Palindrome")