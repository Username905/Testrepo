class base_1():
    pass

class base_2():
    pass

#Этот класс  наследуте сразу от 2 родительских классов(base_make,base_2)

class multi_base(base_1,base_2):
    pass


#Многоуровневая наследование

"""Мы также можем наследовать класс от уже наследогонного"""

"""В многоуровневом наследовании свойства родительского класса и наследуемого от него класса передаются новому наследуемому класса."""