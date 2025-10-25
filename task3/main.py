# Асядовский Станислав
skolko_strok = int(input('Введите количество строк: ')) # прошу ввод количества строк
strochki = [] # создаю список куда запишу строки
count_words = 0 # ввожу счётчик
for stroki in range(skolko_strok): # цикл для ввода строк
    stroki = input("Вводите строки: ")
    strochki.append(stroki) # заполняю список строками
for stroki in strochki: # перебираю строки
    words = stroki.split() # в переменную ворд запишутся слова строк
    count_words += len(words) # счётчик пополняется длинной строки words
print(f'Количество слов в строках - {count_words}') # вывод результата