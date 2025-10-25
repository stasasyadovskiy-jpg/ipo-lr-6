import random
spisok = [random.randint(-50,50) for i in range(25)]
count_plus = 0
count_minus = 0
count_nolik = 0
for i in range(spisok):
    if (spisok[i] > 0):
        count_plus += 1
    elif (spisok[i] < 0):
        count_minus += 1
    else: count_nolik += 1
print("Количество положительных элементов в списке:", count_plus)
print("Количество отрицательных элементов в списке:", count_minus)
print("Количество нулевых элементов в списке:", count_nolik)
