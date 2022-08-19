# 11.28. Выяснить, верно ли, что сумма элементов массива есть неотрицательное число.

import random

arrayRange = 10
array = []
for i in range(arrayRange):
    array.append(random.randint(-10, 10))
print(array)
check = sum(array)
if check > 0:
    print(f"SUM {check} = True")
elif check < 0:
    print(f"SUM {check} = False")
elif check == 0:
    print(f"SUM {check} = 0")
