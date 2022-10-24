#Global and local varables

x = "глобальная переменная"
def foo():
    global x
    y = "локальная переменная"
    x = x * 2
    print(x)
    print(y)
foo()

#Global and local varables с одинаковим именем

num = 5

def foo():
    num = 10
    print()