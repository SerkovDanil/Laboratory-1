numbers = [2, -93, -2, 8, None,-44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
print("Старый список:", numbers)
# TODO заменить значение пропущенного элемента средним арифметическим
b1 = len(set(numbers))
print("количество символов:", b1)

Nid = numbers.index(None)

nev = (sum(numbers[0:Nid]) + sum(numbers[Nid+1:]))/len(numbers)
numbers[Nid] = nev

print("Измененный список:", numbers)