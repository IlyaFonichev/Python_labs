numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_none = [i for i in numbers if i is not None]
numbers = [sum(numbers_none) / len(numbers) if i is None else i for i in numbers]

print("Измененный список:", numbers)
