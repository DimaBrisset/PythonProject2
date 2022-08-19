# 11.45. Дан массив. Вывести на экран сначала его элементы, стоящие на четных местах, затем — на нечетных.

import random

arrayRange = 10
array = []
array2 = []
for i in range(arrayRange):
    array.append(random.randint(-10, 10))
print(array)

print(*(array[::2] + array[1::2]))
