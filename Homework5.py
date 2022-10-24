#1

this_list = ["Iphone","Samsung","Xiaomi"]
this_list.reverse()
print(this_list)

#2

changed_list = [1,2,3,4,5]
new_list = changed_list.pop()
new_list1 = changed_list.pop(0)
changed_list.append(new_list1)
changed_list.insert(0, new_list)
print(changed_list)

#3

def to_list(*args):
    return list(args)
print(to_list(1,2,3,4,5,6))


#4

def useless(lst) :
    return max(lst) / len(lst)
print(useless(5445, 533, 55))

#5

def list_sort(lst) :
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst
print(list_sort(1,88,654,-44,3))