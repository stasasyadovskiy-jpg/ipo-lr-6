# Асядовский Станислав
import random # библиотека рандом
spisok = [random.randint(-50,50) for i in range(25)] # генерирую список
print(f'Список: {spisok}') # вывожу список
# ввожу счётчики
count_plus = 0
count_minus = 0
count_nolik = 0
procent_plus = 0
procent_minus = 0
procent_nolik = 0
print('Положительные элементы: ')
for num in spisok: # цикл для положительных
    if (num > 0): # если элемент больше нуля
        count_plus += 1 # увеличиваем счётчик
        procent_plus = count_plus * 100 / 25 # вычисляем процент
        print(f'{num}') # выводим эти числа
print('Отрицательные элементы: ')
for num in spisok: # цикл для отрицательных
    if (num < 0): # если элемент меньше нуля
        count_minus += 1 # увеличиваем счётчик
        procent_minus = count_minus * 100 / 25 # вычисляем процент
        print(f'{num}') # выводим эти числа
print('Нулевые элементы: ')
for num in spisok: # цикл для нулевых
    if num==0: # если элемент равен нулю
        count_nolik += 1 # увеличиваем счётчик
        procent_nolik = count_nolik * 100 / 25 # вычисляем процент
        print(f'{num}') # выводим эти числа
# вывод нужных значений
print(f"Количество положительных элементов в списке - {count_plus}, их процент - {procent_plus}") 
print(f"Количество отрицательных элементов в списке - {count_minus}, их процент - {procent_minus}")
print(f"Количество нулевых элементов в списке - {count_nolik}, их процент - {procent_nolik}")
print(f'Максимальное значение списка: {max(spisok)}')
print(f'Минимальное значение списка: {min(spisok)}')