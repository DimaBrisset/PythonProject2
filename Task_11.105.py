#11.105.*В массиве из 30 элементов числа образуют неубывающую последовательность.
# Найти количество различных чисел в массиве.
array = [1, 1, 1, 5, 5, 6, 7, 8, 8, 8, 11, 12, 13, 10, 15, 16, 40, 18, 19, 20, 40, 22, 23, 24, 25, 40, 27, 28, 29,
         30]

print(array)
array.sort()
print(array)
countSameNumbers = 0
for i in range(len(array) - 1):
    if array[i] == array[i + 1]:
        countSameNumbers += 1
print(f"Not Same Numbers: {len(array) - countSameNumbers}")
