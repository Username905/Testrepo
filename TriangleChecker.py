class TriangleChecker():

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_triangle(self):
        
        if self.a > 0:
            self.b > 0
            self.c > 0
            print(f"Ура, можно построить треугольник!")
        elif self.a < 0:
            self.b < 0
            self.c < 0
            print(f"С отрицательными числами ничего не выйдет!")
        elif self.a == str:
            self.b == str
            self.c == str
            print(f"Нужно вводить только числа!")
        else:
            Triangle == ""
            print(f"Жаль, но из этого треугольник не сделать.")

Triangle = TriangleChecker("A","f","d")
Triangle.is_triangle()