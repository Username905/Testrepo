#Make a simple calculator



#This funkction adds two numbers


def add(x, y):
    return x + y

#This funkction subract two numbers

def subtract(x, y):
    return x - y

#This funkction multyply two numbers

def multiply(x, y):
    return x * y

#This funkction divide two numbers

def divide(x, y):
    return x / y

print("Select options")
print("+. Add")
print("- Subtract")
print("* Multiply")
print("/ Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(add(num1, num2))

        elif choice == '2':
            print(subtract(num1, num2))

        elif choice == '3':
            print(multiply(num1, num2))

        elif choice == '4':
            print(divide(num1, num2))    

        exit = input("Do you want exit calculation? (yes/no): ")
        if exit == "yes":
          break    
            
    else:
        print("Syntax Error")