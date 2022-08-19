# 11.13
# Cоставить программу вывода на экран любого элемента массива по его индексу.
import random

arrayRange = 10
array = []
for i in range(arrayRange):
    array.append(random.randint(1, 10))
print(array)
while True:
    userInput = int(input("element #: "))
    if userInput <= arrayRange:
        print(array[userInput])
    elif userInput > arrayRange:
        print('not correct input')
