from os import system
from random import choice

# Основна функція, що отримує масив та елемент для пошуку, і повертає список індексів входження цього елементу в масив
# методом грубої сили:
def match_in_massive(massive,element):
    lst = []
    for i in range(len(massive)):       # Перебираємо список індексів масиву
        if massive[i] == element:
            lst.append(i)
    return lst


# Пошук першого входження методом грубої сили, наведений у книзі (Зручно використовувати у низькорівневих мовах
# програмування, таких як С, де немає функції range()):
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


# -----------------------Все нижче - інтерфейс, взаємодія з користувачем:
ans = 1
while ans != "0":
    system("cls")
    print(("Created by: Pankeyeva Sophia, KM-93 \n\n"))
    ans = input("0 - exit\n1 - hand made massive\n2 - random filling\n")      # Користувач вибирає режим заповнення
    if ans == "1" or ans == "2":
        massive = []
        n = int(input("Input lenght of your massive:\n"))           # Вводить довжину масива
        if ans == "1":                                              # Ручне заповнення
            for i in range(n):
                system("cls")
                massive.append(input("Your massive now: {}\nPlease, input {} element: ".format(massive,i+1)))
        elif ans == "2":                                            # Автоматичне заповнення
            for i in range(n):
                massive.append(choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','z','1','2','3','4','5','6','7','8','9','abc','KM','83','lalala','Python','Ruby','JS','Java','Pringles','sofa','Alexandro','Larko_0','Kasi4','fingers']))
        system("cls")
        input("Your massive: {}".format(massive))

        element = input("Input element: ")
        print("List of indexes this element in your massive:\n{}\n\n".format(match_in_massive(massive,element)))
        #Власне використання функції для пошуку елемента
        ans = input("0 - Exit\n1 - Continue\n")                     # Чи продовжуватиме користувач
