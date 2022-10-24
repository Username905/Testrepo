"""Словарь может содержать другие словари, это називается вложеннимы словарями"""

my_family = {
    "Child1" : {
        "Name" : "Mikael",
        "Year" : 1995,
    },
    "Child2" : {
        "Name" : "Aram",
        "Year" : 2003
    },
    "Child3" : {
        "Name" : "Areg",
        "Year" : 2005
    }
}

print(my_family)

"""Создание трех словарей, затем созданые одного словаря которое будет хранить все три словаря"""

Child4 = {
    "Name" : "Mikael",
    "Year" : 1995
},
Child5 = {
    "Name" : "Aram",
    "Year" : 2003
},
Child6 = {
    "Name" : "Areg",
    "Year" : 2005
},

myfamily = {
    "Child4" : Child4,
    "Child5" : Child5,
    "Child6" : Child6,
}

print(myfamily)