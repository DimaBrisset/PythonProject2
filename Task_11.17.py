# 11.17
# Дан массив. Все его элементы:
# а) увеличить в 2 раза;
# б) уменьшить на число А;
# в) разделить на первый элемент.

import random

arrayRange = 10
array = []
array2 = []
array3 = []
array4 = []
for i in range(arrayRange):
    array.append(random.randint(1, 10))
print("Array")
print(array)

for j in range(arrayRange):
    array2.append(array[j] * 2)
print("Array*2")
print(array2)

for k in range(arrayRange):
    array3.append(array[k] / array[0])
print("Array / Array[0]")
print(array3)

a = int(input("Reduce element by: "))
for x in range(arrayRange):
    array4.append(array[x] - a)
print(f"Array - {a}")
print(array4)
