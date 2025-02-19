def main():
    fruit = input("Enter a fruit: ")
    fruit = fruit.lower()
    for item in fruit_list:
        if item['name'] == fruit:
            print('Calories: ', item['calories'])
            break

fruit_list = [
    {'name': 'apple', 'calories': 130}, 
    {'name': 'avocado', 'calories': 50},
    {'name': 'banana', 'calories': 110},
    {'name': 'cantelope', 'calories': 50},
    {'name': 'grapefruit', 'calories': 60},
    {'name': 'grapes', 'calories': 90},
    {'name': 'honeydew', 'calories': 50},
    {'name': 'kiwi', 'calories': 90},
    {'name': 'lemon', 'calories': 15},
    {'name': 'lime', 'calories': 20},
    {'name': 'nectarine', 'calories': 60},
    {'name': 'orange', 'calories': 80},
    {'name': 'peach', 'calories': 60}, 
    {'name': 'pear', 'calories': 100}, 
    {'name': 'pineapple', 'calories': 50},
    {'name': 'plum', 'calories': 70},
    {'name': 'strawberry', 'calories': 50}, 
    {'name': 'cherries', 'calories': 100},
    {'name': 'tangerine', 'calories': 50},
    {'name': 'watermelon', 'calories': 80}
]


main()