# Task 1
with open('file1.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        ingredient_count = int(f.readline())
        ingredients = []
        for i in range(ingredient_count):
            ing = f.readline().strip()
            ingredient_name, quantity, measure = ing.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        f.readline()
        cook_book[dish] = ingredients
print(f'cook_book =\n {cook_book}')


# # Task 2
def get_shop_list_by_dishes(dishes, person_count):
    dishes_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                dishes_dict[ingredient['ingredient_name']] = {'quantity': ingredient['quantity'] * person_count,
                                                              'measure': ingredient['measure']}
    return dishes_dict


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Task 3
full_text = {}
sum_str = {}
with open('1.txt', 'r', encoding='utf-8') as f:
    name = '1.txt'
    sum_ = 0
    str_list = []
    for line in f:
        sum_ += 1
        str_list.append(line)
        full_text[name] = str_list
    sum_str.setdefault(name, sum_)

with open('2.txt', 'r', encoding='utf-8') as f:
    name = '2.txt'
    sum_ = 0
    str_list = []
    for line in f:
        sum_ += 1
        str_list.append(line)
        full_text[name] = str_list
    sum_str.setdefault(name, sum_)

with open('3.txt', 'r', encoding='utf-8') as f:
    name = '3.txt'
    sum_ = 0
    str_list = []
    for line in f:
        sum_ += 1
        str_list.append(line)
        full_text[name] = str_list
    sum_str.setdefault(name, sum_)

# print(full_text)
# print(sum_str)


sorted_dict = {}
sorted_keys = sorted(sum_str, key=sum_str.get)
for i in sorted_keys:
    sorted_dict[i] = sum_str[i]
# print(sorted_dict)


with open('new.txt', 'w', encoding='utf-8') as f:
    for k, v in sorted_dict.items():
        f.writelines(k)
        f.writelines('\n')
        f.writelines(str(v))
        f.writelines('\n')
        key = full_text[k]
        f.writelines(key)
        f.writelines('\n')
