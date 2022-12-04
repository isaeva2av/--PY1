def delete(list_,
           index=None):

    if index is None:
        list_ = list_[:-1]  # пусть по умолчанияю из списка удаляется последний элемент.
    elif index is -1:
        list_ = list_[:-1]  # предусматриваем возможность удаления по отрицательному индексу
    else:
        # С помощью слайсирования разбиваем
        list_ = list_[:index] + list_[index+1:]  # Складываем списки без удаляемого значения
    return list_


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
