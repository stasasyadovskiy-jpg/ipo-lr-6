# Асядовский Станислав
import random # библиотека рандом
spisok = [[random.randint(-10,10) for i in range(4)] for i in range(20)] # генерирую список со списками
tuple_list = [] # создаю список для кортежей
for nums in spisok: # перебираю список
    tuple_list.append(tuple(nums)) # заполняю список кортежей списками из списка
print(f'Список с кортежами: {tuple_list}') # вывожу список кортежей
my_sum = int(input("Введите число для сравнения: ")) # прошу 
pair_sum = 0 # ввожу сумму для пар 
count_pairs = 0 # счётчик пар
for i in range(len(tuple_list)): # перебираю все кортежи из списка
    for j in range(i+1, len(tuple_list)): # перебираю кортеж для пары
        pair_sum = sum(tuple_list[i]) + sum(tuple_list[j]) # считаю сумму пар
        if pair_sum > my_sum: # если сумма пары больше введённого числа
            count_pairs += 1 # увеличиваем счётчик пар
            print(f"Пара {tuple_list[i]} + {tuple_list[j]} = {pair_sum}") # вывожу нужные пары
print(f'Количество пар, сумма которых больше {my_sum} - {count_pairs} ') # вывожу количество пар