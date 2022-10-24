user = input("Enter: ")

check_quantity = len(user)

nums = []

item = 0

while item < check_quantity:
    user_int = "" 
    res = user[item]
    while "0" <= res <= "9":
        user_int += res
        item += 1
        if item < check_quantity:
            res = user[item]
        else:
            break
    item +=1
    if user_int != "":
        nums.append(int(user_int))
print(nums)