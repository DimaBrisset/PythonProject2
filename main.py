#11.9
# Заполнить массив:
#а) десятью первыми членами арифметической прогрессии с известным первым членом прогрессии а и ее разностью р;
#б) двадцатью первыми членами геометрической прогрессии с известным #первым членом прогрессии а и ее знаменателем z;
#в) двенадцатью первыми членами последовательности Фибоначчи (последовательности, в которой первые два члена равны
# 1, а каждый следующий #равен сумме двух предыдущих).

a=int(input())
p=int(input())
myList = [a]
for i in range(1, 10):
    myList.append(a+i*p)
print(*myList)


a=int(input())
z=int(input())
myList = [a]
for i in range(1, 20):
    myList.append((i-1)*z)
print(*myList)


n=12
fibo = [1, 1]
[fibo.append(fibo[-2] + fibo[-1]) for i in range(n - 2)]
print(fibo)
