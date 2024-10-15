 # множества set
set_ = {1,2,3,4,11,22}
set_1 = {11,22,33,44,55}
print(set_)
print(set_1)
set_2 = set_ | set_1
print(set_2)
if 22 in set_:             # если ... в set_: пиши "верно"
    print("верно")
else:                      # иначе: ... пиши "ложь"
    print("ложь")
set_3 = set_1 & set_
print(set_3)
if 33 not in set_3:        # если ... не в set_: пиши "верно"
    print("верно")
else:                       # иначе: ... пиши "ложь"
    print("ложь")

    # преобразование строки в список и обратно
a = list(set_3)
print('a = ', a, type(a))            # множество в список
b = map(str,a)                       # каждый эл. из списка в строку
c = "".join(b)                       # склейка эл. в одну строку
print('c= ', c, type(c))
d = int(c)                           # строку в целые числа
print('d= ',d, type(d))

print(1213)
