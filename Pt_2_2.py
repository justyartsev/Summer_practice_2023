shows = ["Ellen Show", "The Tonight Show", "The Late Late Show", "Night Show"]
for i in range(len(shows)):
    print(shows[i])
new_show = input("Введите название передачи: ")
index = int(input("Введите позицию: ")) - 1
shows.insert(index, new_show)
for i in range(len(shows)):
    print(shows[i])
