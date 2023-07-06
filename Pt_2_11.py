a = int(input("Введите начальное число: "))
b = int(input("Введите конечное число: "))
summ = 0
for i in range(a, b + 1):
    summ += i
print(summ)
