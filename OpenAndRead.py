def read_cookbook(file_path: str) -> dict:
    cook_book = {}
    with open(file_path, encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                line = file.readline().strip()
                ingredient_name, quantity, measure = line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book
print(read_cookbook('recipes.txt'))


