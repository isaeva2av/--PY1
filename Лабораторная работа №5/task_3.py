import random


def get_unique_list_numbers(start, stop, count) -> list[int]:
    list_unique = []  # Создаем список.
    while len(list_unique) < count:  # Пусть длина списка будет не заданного по исходным данным.
        random_int = random.randint(start, stop)  # Генирируем числа из заданного диапозона.
        if random_int not in list_unique:  # Если числа нет в списке,
            list_unique.append(random_int)  # добавляем его в этот список.
    return list_unique


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)  # Задаем исходные данные диапозона и размера списка.
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))  # Проверяем список на уникальность.
