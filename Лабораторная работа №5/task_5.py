from random import sample
import string


def get_random_password(length) -> str:
    # Генирируем значения с помощью первой константы (буквами верхнего, нижнего регистра), и второй - цифры.
    random_password = string.ascii_uppercase + string.ascii_lowercase + string.digits
    random_string = ''.join(random.sample(random_password, length))  # Формируем случайную строку определенной длины.
    return random_string


print(get_random_password(8))  # Выводим результат, задав длину пароля.
