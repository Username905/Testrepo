"""List"""

#1

cars = ["BMW","Mercedes","Jaguar","Pagani","Koenigsegg","Dodge"]
print(cars)
print(type(cars))
print(len(cars))

#2

citys = ["London","Moscow","Los_Angeles:)","Washington","Kuala Lumpur"]
print(citys)
print(type(citys))
print(len(citys))

#3

buildings = ["Burj-Khalifa","Empire State Building","Tower of Eifel"]
print(buildings)
print(type(buildings))
print(len(buildings))

#4

museums = ["Louvre" , "Ermitage" , "Prada","National Gallery of Armenia"]
print(museums)
print(type(museums))
print(len(museums))

#5

fruties = ["apple","orange","pinapple","mango","avocado"]
print(fruties)
print(type(fruties))
print(len(fruties))

#6

drinks = ["Jack Daniels","Chivas","Aperol","Campari","Bacardi"]
print(drinks)
print(type(drinks))
print(len(drinks))

#7

systems = ["Linux","Windows","MacOS"]
print(systems)
print(type(systems))
print(len(systems))

#8

rappers = ["Tupac","Notorious Big","Eminem","Miyagi","Andy Panda"]
print(rappers)
print(type(rappers))
print(len(rappers))

#9

in_my_table = ["JBL","AirPods","Cola"]
print(in_my_table)
print(type(in_my_table))
print(len(in_my_table))

#10

just_list = ["cactus","cup","gun"]
print(just_list)
print(type(just_list))
print(len(just_list))


"""Tuple"""

#1

mix = ("JBL","Tupac","gun")
print(mix)
print(type(mix))
print(len(mix))

#2

mix1 = ("BMW","Moscow","gun")
print(mix1)
print(type(mix1))
print(len(mix1))

#3

mix2 = ("cactus","Bacardi","Louvre")
print(mix2)
print(type(mix2))
print(len(mix2))

#4

mix3 = ("Kuala Lumpur","Mercedes","Tower of Eifel")
print(mix3)
print(type(mix3))
print(len(mix3))

#5

mix4 = ("Burj Khalifa","Pagani","Chivas")
print(mix4)
print(type(mix4))
print(len(mix4))

#6

mix5 = ("Jack Daniels","Cola","Miyagi")
print(mix5)
print(type(mix5))
print(len(mix5))

#7

fresh = ("Orange","Apple")
print(fresh)
print(type(fresh))
print(len(fresh))

#8

mix6 = ("Dodge","avocado","mango","Bacardi")
print(mix6)
print(type(mix6))
print(len(mix6))

#9

mix7 = ("Nationa Gallery of Armenia","BMW","Ermitage")
print(mix7)
print(type(mix7))
print(len(mix7))

#10

mix8 = ("Windows","Eminem","AirPods","cup")
print(mix8)
print(type(mix8))
print(len(mix8))

"""Dictionary"""

#1

info = {
    "building" : "Burj Khalifa",
    "Height" : 828,
    "floors" : 163
}

print(info)
print(type(info))
print(len(info))

#2

info1 = {
    "car" : "Pagani",
    "model" : "Huaryra",
    "hp" : 700,
    "price" : 1.300
}

print(info1)
print(type(info1))
print(len(info1))

#3

info2 = {
    "museum" : "Louvre",
    "established" : 1793,
    "exponats" : 300.000
}

print(info2)
print(type(info2))
print(len(info2))

#4

info3 = {
    "brand" : "Chivas",
    "Type" : "Whiskey",
    "introduced" : 1801,
    "country of origin" : "Scotland"
}

print(info3)
print(type(info3))
print(len(info3))

#5

info4 = {
    "name" : "Tupac",
    "date of birth" : 1971,
    "country" : "USA"
}

print(info4)
print(type(info4))
print(len(info4))

#6

info5 = {
    "name" : "Areg",
    "lastname" : "Shahumyan",
    "age" : 17
}

print(info5)
print(type(info5))
print(len(info5))

#7

info6 = {
    "brand" : "Mercedes",
    "model" : "E63s",
    "hp" : 575
}

print(info6)
print(type(info6))
print(len(info6))

#8

info7 = {
    "brand" : "Jack Daniels",
    "type" : "Whiskey",
    "founded" : 1866
}

#9

info8 = {
    "brand" : "Koenigsegg",
    "model" : "Agera",
    "hp" : 1340
}

#10

info9 = {
    "language" : "python",
    "creator" : "Guido Van Rossum",
    "crated_in" : 2005
}


"""Set"""

#1

mix_1 = {"BMW","London","Burj Khalifa"}
print(mix_1)
print(type(mix_1))
print(len(mix_1))

#2

mix_2 = {"Louvre","apple","Jack Daniels"}
print(mix_2)
print(type(mix_2))
print(len(mix_2))

#3

mix_3 = {"Linux","Tupac","JBL","cactus"}
print(mix_3)
print(type(mix_3))
print(len(mix_3))

#4

mix_4 = {"cup","Prada","Tower of Eifel"}
print(mix_4)
print(type(mix_4))
print(len(mix_4))

#5

mix_5 = {"Washington","pinapple","mango",1}
print(mix_5)
print(type(mix_5))
print(len(mix_5))

#6

mix_6 = {"avocado","Aperol","Campari",987.3}
print(mix_6)
print(type(mix_6))
print(len(mix_6))

#7

mix_7 = {"Windows","MacOS","Miyagi","&","Andy Panda"}
print(mix_7)
print(type(mix_7))
print(len(mix_7))

#8

mix_8 = {"Tecuila","salt","lemon",17}
print(mix_8)
print(type(mix_8))
print(len(mix_8))

#9

mix_9 = {"Deel","Linux","Python",15}
print(mix_9)
print(type(mix_9))
print(len(mix_9))

#10

mix_10 = {"Python","C++","C#"}
print(mix_10)
print(type(mix_10))
print(len(mix_10))


"""FrozenSet"""

#1

f_mix1 = frozenset(mix1)
print(f_mix1)
print(type(f_mix1))
print(len(f_mix1))

#2

f_mix2 = frozenset(mix3)
print(f_mix2)
print(type(f_mix2))
print(len(f_mix2))

#3

f_mix3 = frozenset(mix8)
print(f_mix3)
print(type(f_mix3))
print(len(f_mix3))

#4

f_mix4 = frozenset(mix4)
print(f_mix4)
print(type(f_mix4))
print(len(f_mix4))

#5

f_mix5 = frozenset(mix7)
print(f_mix5)
print(type(f_mix5))
print(len(f_mix5))

#6

f_mix6 = frozenset(mix6)
print(f_mix6)
print(type(f_mix6))
print(len(f_mix6))

#7

f_mix7 = frozenset(mix2)
print(f_mix7)
print(type(f_mix7))
print(len(f_mix7))

#8

f_mix8 = frozenset(mix_5)
print(f_mix8)
print(type(f_mix8))
print(len(f_mix8))

#9

f_mix9 = frozenset(mix_2)
print(f_mix9)
print(type(f_mix9))
print(len(f_mix9))

#10

f_mix10 = frozenset(mix_7)
print(f_mix10)
print(type(f_mix10))
print(len(f_mix10))