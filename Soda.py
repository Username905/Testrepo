class Soda():
    """для определения класса газировки"""
    
    def __init__(self,dobavochka):
        self.dobavochka = dobavochka
    
    def show_my_drink(self):
        print(f"<<Газировка и {self.dobavochka}>>")
        if {self.dobavochka} != "":
            print("Газировка с добавкой")
        else:
            {self.dobavochka} == ""
            print("обычная газировка")

Juice = Soda("Orange")

Juice.show_my_drink()