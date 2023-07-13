import csv

book_header = "Книга"
author_header = "Автор"
release_year_header = "Год выпуска"
with open("Book.csv", mode="w") as csv_file:
    headers = [book_header, author_header, release_year_header]
    file_writer = csv.DictWriter(csv_file, delimiter=" ", lineterminator="\r", fieldnames=headers)
    file_writer.writeheader()
    number = int(input("Введите количество записей: "))
    for i in range(number):
        book = input("Введите название книги: ")
        author = input("Введите имя автора: ")
        year = int(input("Введите год выпуска: "))
        file_writer.writerow({book_header: book, author_header: author, release_year_header: year})
        print(f"Запись номер {i + 1} сформирована")
with open("Book.csv") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=" ")
    find_author = input("Введите нужного вам автора: ")
    count = 0
    print(reader)
    for row in reader:
        if find_author == row[author_header]:
            print(row[book_header], row[author_header], row[release_year_header])
            count += 1
    if count == 0:
        print("В списке нет книг данного автора!")
