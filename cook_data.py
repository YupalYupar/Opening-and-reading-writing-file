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

print()#3 Задание
from pprint import pprint
all_txt = ['1.txt','2.txt','3.txt']

def all_txt_reader(all_txt):
    mainfile_alldict = {}
    file_alldict = {}
    for each_list in all_txt:
        with open (each_list, encoding='utf-8') as one_file:
            file_list = []
            b = len(file_list)
            for i in one_file:
                file_list.append(i.strip())
                b = str(len(file_list))
            convertList = ' '.join([str(e) for e in file_list])
            file_alldict = (b, convertList,)
            mainfile_alldict[each_list] = file_alldict
            sorted_file = sorted(mainfile_alldict.items(), key=lambda x:x[1],reverse = True)
    return(sorted_file)

pprint(all_txt_reader(all_txt))


result_file = 'result.txt'
def result_writing(result_file, w ):
    with open(result_file, w , encoding='utf-8') as file:
        for i in all_txt_reader(all_txt):
            file.write(f'\n')
            file.write(f'{i[0]}\n')
            file.write(f'{i[1][0]}\n')
            for line in range(int(i[1][0])):
                file.write(f'Строка номер {line+1} файла номер {i[0][0]}\n')

result_writing(result_file, 'w' )
