age = int(input("какой у тебя возраст: "))
idcard = str(input("\nу тебя есть ид карта: "))
if age >= 18 and idcard == "да" :
    print("\nможешь зажодить")
else:
    print("\nты не можешь заходить")
