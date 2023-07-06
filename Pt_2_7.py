summ = 0
while True:
    number = int(input("Введите отрицательное число: "))
    if number < 0:
        summ += number
        print(f"Текущая сумма равна {summ}")
    else:
        print("Данное число - неотрицательное")
        break
