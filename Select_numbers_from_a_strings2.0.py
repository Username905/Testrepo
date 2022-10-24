user = input("Enter: ")

nums = []

num = ""

for item in user:
    if item.isdigit():
        num = num + item
        