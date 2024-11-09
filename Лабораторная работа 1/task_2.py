# TODO Найдите количество книг, которое можно разместить на дискете
memory = 1024 * 1024 * 1.44
data = 4 * 25 * 50 * 100
quantity_of_books = int(memory // data)
print("Количество книг, помещающихся на дискету:", quantity_of_books)
