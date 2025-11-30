# Создание словаря из файла
def read_cookbook(file_path: str) -> dict:
    cook_book = {}
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
            cook_book[name] = ingredients
            # Пропускаем пустую строку
            file.readline()
    return cook_book

cook_book = read_cookbook('recipes.txt')


# Функция кол-ва ингредиентов на каждую персону
def get_shop_list_by_dishes(dishes: list, person_count: int, cook_book: dict) -> dict:
    shop_list_by_dishes = {}
    for dish in dishes:
        # Если блюда нет в книге рецептов
        if dish not in cook_book:
            print(f'{dish} нет в книге рецептов')
            continue
        # Перебор ингредиентов
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            # Если ингредиента нет - присваиваем ему ключ(название) и значение (Ед. измерения и кол-во)
            if name not in shop_list_by_dishes:
                shop_list_by_dishes[name] = {'measure': measure, 'quantity': quantity}
            # Если есть - добавляем кол-во
            else:
                shop_list_by_dishes[name]['quantity'] += quantity
    return shop_list_by_dishes

shop_list_by_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(shop_list_by_dishes)



