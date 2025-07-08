from operator import index

my_list = [1, 2]
my_tuple = (1, 2, 3)
a = my_list[0]
b = my_list[1]
c = my_tuple[0]
d = my_tuple[1]
e = my_tuple[2]
print(a, b, c, d, e)


#выгрузка из списка и кортежа
a, b = my_list
c, d, e = my_tuple
print(a, b, c, d, e)

# Срез  позволяет выбрать конкеретые значения из списка или кортежа
lll = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(lll)
print(lll[5:])
print(lll[1::2])
print(lll[::-1])
print(lll[-2:-6:-1])

text = 'Первый второй третий'
print(text[0:])
print(len(text))
print(text.index('й'))
print(text.count('р'))
print(text.find('fsdsf'))
print(text[:8])
print(text[::2])
print(text[::-1])

print(text.startswith("Второй"))
lll = lll - lll