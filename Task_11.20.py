#11.20 11.20. Дан массив a. Определить знакопеременную сумму a1-a2+a3-a4
#Условный оператор и операцию возведения в степень не использовать.
import random

arrayRange = 10
array = []
for i in range(arrayRange):
    array.append(random.randint(-10, 10))
print(array)
summa = 0
check = 1
for i in range(len(array)):
    summa += check * array[i]
    check *= -1
print(summa)
