#11.104  массиве из 20 элементов числа образуют неубывающую последовательность. Несколько элементов, идущих подряд, равны между собой. Найти
#количество таких элементов. Сколько различных чисел имеется в массиве?
array = [1, 1, 3, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
countSameNumbers = 0

print(array)
for i in range(len(array) - 1):
    if array[i] == array[i + 1]:
        countSameNumbers += 1
print(f"Same Numbers: {countSameNumbers}")
print(f"Not Same Numbers: {len(array) - countSameNumbers}")
