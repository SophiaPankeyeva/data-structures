# Пошук першого входження методом грубої сили, наведений у книзі (Зручно використовувати у низькорівневих мовах
# програмування, таких як С, де немає функції range()):
from random import randrange
from time import time
def match_from_book(massive, element):
    i = 0
    while i < len(massive) and massive[i] != element: # (*)Наявна зайва перевірка на кожній ітераціїї: i < len(massive)
        i += 1
    if i == len(massive):
        return "Massive have not this element"
    else:
        return i


# Невелике покращення ефективності алгоритму шляхом додавання шуканого елементу в кінець масиву, задля уникнення (*)
# перевірки i < len(massive) на кожній ітерації циклу
def match_from_book1(massive, element):
    i = 0
    massive.append(element)       # Додаємо шуканий елемент в кінець масиву
    while massive[i] != element:
        i += 1
    if i == len(massive) - 1:
        return "Massive have not this element"
    else:
        return i

mass1 = []
for i in range(10000000):
    mass1.append(1)
    
mass1.append(-5)
mass1.append(-3)

input("First test")
time1 = time()
print(match_from_book(mass1, -5))
time1_delta = time() - time1
print("Time: ",time1_delta)
input("Second test")
time2 = time()
print(match_from_book1(mass1, -5))
time2_delta = time() - time2
print("Time: ",time2_delta)
input()
time_d = time1_delta - time2_delta
print("Second algorythm on 10 000 000 elements is faster than first for {} seconds".format(time_d))
input()
