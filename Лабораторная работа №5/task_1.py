from pprint import pprint
# Создаем список из словарей.
list1 = [
    {
        'bin': bin(num),
        'dec': num,
        'hex': hex(num),
        'oct': oct(num),
    }
    for num in range(0, 16)  # Создаем словари для промежутка чисел.
]
pprint(list1)
