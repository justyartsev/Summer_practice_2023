number = int(input("Введите число: "))
mas = []
for i in range(len(str(number))):
    mas.append(number % 10)
    number = number // 10
print(f"{mas.index(max(mas)) + 1} - индекс максимального элемента с конца")
mas.reverse()
print(f"{mas.index(max(mas)) + 1} - индекс максимального элемента с начала")
