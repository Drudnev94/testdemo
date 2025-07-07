
from random import choice
list1 = (1, 2, 3)
list2 = ("кошка", "собака", "конь")
list3 = ("ребенок", "женшина", "Мужчина")


def rand():
    a = choice(list1)
    b = choice(list2)
    c = choice(list3)
    return a, b, c

resul = rand()
print(resul)


