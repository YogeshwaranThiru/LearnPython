# Size of shopping list
# 3
# Enter item 1: apple
# Enter item 2: banana
# Enter item 3: cat
# Print shopping listput 

shopping_list_size = int(input("Plz enter shopping list size : ")) 
shopping_list = []

while len(shopping_list)< shopping_list_size:
    item_number_str = str(len(shopping_list) +1)
    prompt = 'Enter item ' + item_number_str + " : "
    shopping_item = input(prompt)
    shopping_list.append(shopping_item)

print("Shopping list is: ")
print(shopping_list)