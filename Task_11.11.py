# 11.11 Ильзуя датчик случайных чисел, заполнить массив из двадцати элементов неповторяющимися числами.

import random

array = []
array2 = []
array3 = []

for i in range(40):
    array.append(random.randint(-100, 100))
for i in array:
    if i not in array2:
        array2.append(i)

array3 = array2[0:20:1]
print(sorted(array3))
