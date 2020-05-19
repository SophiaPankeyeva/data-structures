count = 0

#----------- Функція для знаходження першого входження підрядка методом грубої сили
def my_match(text, pattern):
    global count
    for i in range(len(text) - len(pattern) + 1):
        j = 0
        count+=1
        while j < len(pattern) and text[i+j] == pattern[j]:
            count+=1
            j+=1
        if j == len(pattern):
            return (i, i+j-1)
    return "No matches"

text = "THERE_IS_MORE_TO_LIFE_THAN_INCREASING_ITS_SPEED"
pattern = "GANDHI"
print(my_match(text,pattern))
print("Count:",count)
