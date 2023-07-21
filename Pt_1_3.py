first_number = int(input("Введите число: "))
second_number = int(input("Введите число: "))
third_number = int(input("Введите число: "))
print("Наибольшее число:",
      max(first_number, second_number, third_number))
print(max(first_number, second_number, third_number),
      first_number + second_number + third_number - max(first_number,
      second_number, third_number) - min(first_number, second_number,
      third_number), min(first_number, second_number, third_number))
