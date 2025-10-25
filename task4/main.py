# Асядовский Станислав
stroka = input('Введите строку для поиска: ') # прошу ввод строки
count_string = 0 # ввожу счётчик
file = open('text.txt', 'r', encoding = "utf-8") # Открываю файл
strings_for_sort = [] # ввожу список для строк которые буду сортировать
for string_file in file: # цикл для перебора строчек
    string = file.readline() # в переменную записываю строчки файла
    if stroka in string: # если нужная строка есть в строчках файла
        strings_for_sort.append(string) # заполняем список этими строчками
sorted_string = sorted(strings_for_sort) # сортируем эти строчки
for string in sorted_string: # цикл для нкжной строки в отсортированных строчках
    count_string += 1 # прибавляем счётчик
    print(string) # выводим строчки текста
print(f'Количество строк с искомой строкой - {count_string}') # выводим счётчик