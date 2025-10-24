# Асядовский Станислав
import random
rows = 4
cols = rows
nums = [-15, -4, -2, -7, 0, 3, 5, 12, 7]
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.choice(nums))
         matrix.append(row)

for i in range(rows):
    for j in range(cols):
        print(f"{matrix[i][j]:4}", end="")