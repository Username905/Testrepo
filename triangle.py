"""Площадь прямоугольника, треугольника и круга"""



print('1: Прямоугольник, 2: Треугольник, 3: Круг')

enter_figure = input("Выберите пожалуйста нужную вам фигуру:  ")

if enter_figure == '1':
    print("Длина сторон прямоугольника: ")
    first_side = int(input("first_side = "))
    second_side = int(input("second_side = "))
    result_area = (first_side + second_side) * 2
    print(f"Ваш результат: {result_area}")
elif enter_figure == "2":
    print("Площадь треугольника:")
    main_side = int(input("main_side = "))
    height_side = int(input("height_side = "))
    result_area1 = 0.5 * (main_side * height_side)
    print(f"Ваш результат: {result_area1}")
elif enter_figure == '3':
    print("Площадь круга:")
    diameter_circle = int(input("diameter_circle = "))
    result1 =  diameter_circle / 2 
    print(f"Ваш результат: {result1}")