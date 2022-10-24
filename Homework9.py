list1 = ["Moscow","London","Paris","Skopje","Washington","Yerevan","Tbilisi"]

list2 = ["Berlin","Kiev","Ottava","Washington","Skopje","Yerevan","Kuala-Lumpur"]

list_t = []

for c in list1:
    for y in list2:
        if c == y:
            list_t.append(c)
            break

print(list_t)

lenght = len(list_t)

print(lenght)