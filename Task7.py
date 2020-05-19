from os import system

#----------- Функція для знаходження кількості всіх входжень підрядка в рядок
def my_matches_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        result = True
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                result = False
                break
        if result == True:
            count += 1
    return count


text = input(" Created by: Pankeyeva Sophia , KM-93\n\nInput text:\n")

while text != "stop":
    pattern = input("Input pattern:\n")
    
    print("Count of your matches: {}".format(my_matches_count(text, pattern)))
    
    input("\nPress Enter")
    system("cls")

    text = input("Input text:\n")
