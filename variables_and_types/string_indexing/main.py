grocery_item = "Grilled Chicken Salad"
length_of_item = len(grocery_item)
first_char = grocery_item[0]
second_char = grocery_item.split()[1][0]
third_char = grocery_item.split()[2][0]
last_char1 = grocery_item.split()[-1][-1]
last_char2 = grocery_item.split()[-2][-1]
last_char3 = grocery_item.split()[-3][-1]
# Testing
print("Length of item name:", length_of_item)
print("First character of each word:", first_char, second_char, third_char)
print("Last character of each word:", last_char1, last_char2, last_char3)