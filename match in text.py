from os import system


#----------- Функція для знаходження першого входження підрядка в рядок способом, представленим у книзі
def my_match_from_book(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        j = 0
        while j < len(pattern) and text[i+j] == pattern[j]:
            j+=1
        if j == len(pattern):
            return (i, i+j-1)
    return "No matches"


#----------- Функція для знаходження першого входження підрядка в рядок методом грубої сили з використанням
# особливостей Пайтона та циклу for замість while
def my_match(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        result = True
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                result = False
                break
        if result == True:
            return (i,i+len(pattern) - 1)
    return "No matches"


#----------- Функція для знаходження списку всіх входжень підрядка в рядок
def my_all_matches(text, pattern):
    lst = []
    for i in range(len(text) - len(pattern) + 1):
        result = True
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                result = False
                break
        if result == True:
            lst.append((i,i+len(pattern) - 1))
    return lst


text = input("Created by: Pankeyeva Sophia , KM-93\n\nInput text:\n")

while text != "stop":
    pattern = input("Input pattern:\n")
    
    print("Your match:\n{}".format(my_all_matches(text, pattern)))
    
    #print("Your match:\n{}".format(my_match_from_book(text, pattern)))
    
    #print("Your match:\n{}".format(my_match(text, pattern)))
    
    input("\nPress Enter")
    system("cls")

    text = input("Input text:\n")
