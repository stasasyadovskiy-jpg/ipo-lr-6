# Асядовский Станислав
import random # подключаем библиотеку для рандомных чисел
rows = random.randint(4, 8) # рандомнок количество строк
cols = random.randint(4, 8) # и столбцов
nums = [-15, -4, -2, -7, 0, 3, 5, 12, 7] # список значений
matrix = [] # создаём пустой список куда запишем матрицу
for i in range(rows): # перебираем строки
    row = [] # создаём пустую строку
    for j in range(cols): # перебираем столбцы
        row.append(random.choice(nums)) # добавляем числа в строку
    matrix.append(row) # добавляем строку в матрицу
print("Матрица:") 
for row in matrix: # перебираем строки матрицы
    for num in row: # перебираем числа в строке
        print(f"{num:4}", end="") # форматированный вывод
    print() # переход на новую строку
odd_sum = sum(num for row in matrix for num in row if num % 2 != 0)
print("Сумма всех нечётных элементов:", odd_sum) # вывод результата