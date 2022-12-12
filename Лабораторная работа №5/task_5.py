from random import sample
from string import ascii_uppercase, ascii_lowercase, digits


def get_random_password(length) -> str:
    # Генирируем значения с помощью первой константы (буквами верхнего, нижнего регистра), и второй - цифры.
    random_password = ascii_uppercase + ascii_lowercase + digits
    random_string = ''.join(sample(random_password, length))  # Формируем случайную строку определенной длины.
    return random_string


print(get_random_password(8))  # Выводим результат, задав длину пароля.
