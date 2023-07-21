distance = int(input("Сколько километров хотите проехать: "))
consumption = int(input(
    "Сколько литров топлива расходует машина на 100 километров: "))
fuel = int(input("Сколько литров топлива в вашем баке: "))
need_fuel = (distance * consumption) / 100
if fuel == need_fuel:
    print("Топлива хватит, чтобы проехать желаемое расстояние.")
else:
    print("Вам не хватит топлива, заправьтесь.")
