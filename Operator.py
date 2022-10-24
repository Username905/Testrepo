'''1.орефметическиы операторы(+сложение,-вичтение,*умножение,/ диление,** развидение степени,// диление без остатков)
   2.опертаоры сравнения
   3.операторы присвоения 
   4.логическиые операторы
   5.операторы принадлежности(in-в,not in-вне,)
   6.оператор тождественности(Is,is not)
   7.логические операторы(And-и,or-или,not-нет)
   8.операторы сравнения(Меньше (<)Больше (>)Меньше или равно (<=)Больше или равно (>=)Равно (==)Не равно (!=))'''

   #орефм операторы
num = 8
num2 = 4
result = num+num2 
print(result)

num3 = 13
num4 = 7
result1 = num3-num4
print(result1)

num5 = 3
num6 = 8
result2 = num5*num6
print(result2)

num7 = 5
num8 = 7
result3 = num7**num8
print(result3)

num9 = 32
num10 = 4
result4 = num9/num10
print(result4)

num11 = 27
num12 = 8
result5 = num11//num12
print(result5)

num13 = 66
num14 = 8
result6 = num13%num14
print(result6)

#опер. прис.

a = 6
b = 9
ab = a < b
ab1 = a > b
ab2 = a <= b
ab3 = a >= b
ab4 = a == b
ab5 = a != b
print(ab)
print(ab1)
print(ab2)
print(ab3)
print(ab4)
print(ab5)

#лог. опер.
'''And hnaravorutyun e talis stugel 2 payman, ete 2 paymannel tru(chisht) en patasxane klini tru, ete pay. 1e sxal e patasxany klini false'''

two_cond = 9 > 9 and 4 > -2
print(two_cond)
# op. ori. jamanak ete pay. 1e chisht e apa patasxany chisht e
two_cond2 = 9 > 9 or 4 > -2
print(two_cond2)

#ete 1 arjeqy 2rd arjeqy chi patasaxany klini false, ete 1in arjeqy nuyn 2rd arjeqna pat. klini true
num16 = 10
num17 = 10
result7 = num16 is num17
result8 = num16 is not num17
print(result7)
print(result8)