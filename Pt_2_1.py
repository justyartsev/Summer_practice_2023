from random import choice

purple = "фиолетовый"
green = "зеленый"
yellow = "желтый"
black = "черный"
blue = "синий"
color = choice([purple, green, yellow, black, blue])
while True:
    your_color = input("Введите цвет: ")
    if your_color == color:
        print("Отлично!")
        break
    else:
        print("Выбери другой цвет")
