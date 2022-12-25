import json

INPUT_FILE = "input_.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:
        rows = [line.strip(new_line).split(delimiter) for line in f]  # Делим полученные данные на части.

    headers = rows.pop(0)  # Вытаскиваем заголовки из файла данных, и удаляем его из файла.

    list_ = [dict(zip(headers, i)) for i in rows]  # Объединяем данные в один список.

    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
