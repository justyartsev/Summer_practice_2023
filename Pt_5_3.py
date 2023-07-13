import csv

book_header = "Книга"
author_header = "Автор"
release_year_header = "Год выпуска"
with open("Book.csv", mode="w") as csv_file:
    headers = [book_header, author_header, release_year_header]
    file_writer = csv.DictWriter(csv_file, delimiter=" ", lineterminator="\r", fieldnames=headers)
    file_writer.writeheader()
    file_writer.writerow({book_header: "Мактуб", author_header: "Пауло Коэльо", release_year_header: 1994})
    file_writer.writerow({book_header: "Мирный воин", author_header: "Дэн Миллмэн", release_year_header: 1980})
    file_writer.writerow({book_header: "Сказки о силе", author_header: "Карлос Кастанеда", release_year_header: 1974})
with open("Book.csv") as csv_file:
    reader = list(csv.DictReader(csv_file, delimiter=" "))
    start_year = int(input("Введите год начала отсчета: "))
    end_year = int(input("Введите год конца отсчета: "))
    for row in reader:
        if start_year <= int(row[release_year_header]) <= end_year:
            print(row[book_header], row[author_header], row[release_year_header])