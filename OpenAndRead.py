# Создание словаря из файла
def read_cookbook(file_path: str) -> dict:
    cook_book_dict = {}
    with open(file_path, encoding='utf-8') as file:
        while True:
            # Название блюда
            name = file.readline().strip()
            if not name:
                break
            # Кол-во ингредиентов
            ingredient_count = int(file.readline().strip())
            ingredients = []
            # Список ингредиенты
            for _ in range(ingredient_count):
                line = file.readline().strip()
                ingredient_name, quantity, measure = line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            # Добавляем список ингредиентов к названию блюда
            cook_book_dict[name] = ingredients
            # Пропускаем пустую строку
            file.readline()
    return cook_book_dict

cook_book = read_cookbook('recipes.txt')


# Функция кол-ва ингредиентов на каждую персону
def get_shop_list_by_dishes(dishes: list, person_count: int, cook_book_dct: dict) -> dict:
    shop_list_by_dishes = {}
    for dish in dishes:
        # Если блюда нет в книге рецептов
        if dish not in cook_book_dct:
            print(f'{dish} нет в книге рецептов')
            continue
        # Перебор ингредиентов
        for ingredient in cook_book_dct[dish]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            # Если ингредиента нет - присваиваем ему ключ(название) и значение (Ед.измерения и кол-во)
            if name not in shop_list_by_dishes:
                shop_list_by_dishes[name] = {'measure': measure, 'quantity': quantity}
            # Если есть - добавляем кол-во
            else:
                shop_list_by_dishes[name]['quantity'] += quantity
    return shop_list_by_dishes

shop_list_by_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
# print(shop_list_by_dishes)


# Функция объединение файлов
def merge_files(input_files: list, output_file: str):
    files_data = []
    # Читаем содержимое каждого файла
    for file_name in input_files:
        with open(file_name, encoding='utf-8') as file:
            # Читаем и разделяем содержимое на строки (если есть переносы строк)
            lines = file.read().split('\n')
            # Убираем пустые строки
            lines = [line for line in lines if line.strip()]
            # Добавляем данные кортежами в список
            files_data.append((file_name, len(lines), lines))
    # Сортировка файлов по количеству строк
    files_data.sort(key = lambda x: x[1])
    # Запись отсортированных данных в результирующий файл
    with open(output_file, 'w', encoding='utf-8') as result:
        # Разделение и запись 3 элементов кортежa из списка
        for file_name_out, line_count_out, lines_out in files_data:
            # Запись 1-(Название файла) и 2-(Кол-во строк) элемента кортежа
            result.write(f"{file_name_out}\n"
                         f"{line_count_out}\n")
            # Распаковка и запись 3-(Список текста) элемента кортежа
            for line in lines_out:
                result.write(f"{line}\n")

# Список файлов для объединения в новый файл
merge_files(['1.txt', '2.txt', '3.txt'], 'result.txt')

with open('result.txt', encoding='utf-8') as result:
    print(result.read())

