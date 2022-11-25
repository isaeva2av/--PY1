list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
max_number = list_numbers[max_index]
current_number = 0

for i, current_number in enumerate(list_numbers):  # используем для получения пары индекс - значение
    if current_number >= max_number:  # если текущее значение больше того, который встречали ранее
        max_index = i  # то перезаписываем индекс максимального числа
        max_number = list_numbers[max_index]
# Используем множественное присваивание для того, чтобы поменять местами элементы.
list_numbers[max_index], list_numbers[-1] = current_number, max_number
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
