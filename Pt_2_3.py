number = int(input("Введите число: "))  # 153
count = 0
delete = number
for i in range(len(str(number))):
    end = delete % 10
    count += end ** len(str(number))
    delete = delete // 10
if count == number:
    print(f"Число {number} - число Армстронга.")
else:
    print(f"Число {number} не является числом Армстронга.")
