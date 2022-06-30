from pprint import pprint


recipe_data = "recipes.txt"
cook_book = {}
def cooking_catalog(recipe_data):
    with open(recipe_data,encoding='utf-8') as file:
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
print() #2 задание

def get_shop_list_by_dishes(dishes, person_count):
  manu = {}
  for food in dishes:
    for foodstuff in cook_book[food]:
      ingredient_name, quantity, measure = foodstuff.values()
      if ingredient_name in manu:
        manu[ingredient_name]["quantity"] += (int(quantity) * person_count)
      else:
         manu[ingredient_name] = {"measure": measure, "quantity": (int(quantity) * person_count)}
  pprint(manu)
get_shop_list_by_dishes(['Омлет','Омлет'], 2)
