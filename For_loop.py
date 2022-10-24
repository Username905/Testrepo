"""Python For loops"""

"""Цикл for используется для перебора последственносты то есть лист,тупле,дикт,сет и стринг"""

cars = ["BMW","Mercedes","Tesla","Dodge","Ford"]

for car in cars: 
    print(car)

for o in "orange":
    print(o)

#The break statmans

"""С помощю оп. break мы можем остановить цикл for до того как он пройдот через все элементы"""

Cities = ["Berlin","London","Paris","Moscow"]

for city in Cities:
    print(city)
    if city == "Paris":
        break 

#Continue statmans

"""С помощю оп. continue, мы можем остановить интерацию и продолжить с следуйшей"""

countries = ["USA","Canada","Mexica","Argentina"]
for country in countries:
    if country == "Canada":
        continue
    print(country)