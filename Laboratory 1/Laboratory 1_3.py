# TODO Найдите количество книг, которое можно разместить на дискете

storageMb = 1.44  # Информационный объем дискеты равен
q = 100  # Количество страниц в книге
w = 50  # Число строк на странице
e = 25  # Количество символов в строке
r = 4   # Для хранения кода одного символа нужно

book = (q * w * e) * r
print(" Размер одной книги:", book, "B")
storageB = storageMb*1024*1024
print(" объем дискеты:", storageB, "B")


t1 = round(storageB/book)
print("Количество книг, помещающихся на дискету:", t1)
