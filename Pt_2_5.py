from random import randint

win = 0
lose = 0
while True:
    random_number = randint(0, 1)
    your_number = int(input("Орел(0) или решка(1): "))
    if your_number == 0 or your_number == 1:
        if your_number == random_number:
            win += 1

            print(f"Счет {win}:{lose}")
            if win == 3:
                print(f"Победа со счетом {win}:{lose}")
                break
        if your_number != random_number:
            lose += 1
            print(f"Счет {win}:{lose}")
            if lose == 3:
                print(f"Поражение со счетом {win}:{lose}")
                break
    else:
        print("Конец игры!")
        break
