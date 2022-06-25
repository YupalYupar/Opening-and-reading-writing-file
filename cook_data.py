from pprint import pprint


recipe_data = "recipes.txt"

def cooking_catalog(recipe_data):
    with open(recipe_data,encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            cook_book[dish] = []
            for ingredient in range(int(file.readline())):
                food = file.readline()
                food_list = food.split("|")
                food_dict = {}
                food_dict['ingredient_name'] = food_list[0]
                food_dict['quantity'] = food_list[1]
                food_dict['measure'] = food_list[2].strip()
                #print(food_dict)
                cook_book[dish].append(food_dict)


            file.readline()
    pprint(cook_book)

cooking_catalog(recipe_data)
