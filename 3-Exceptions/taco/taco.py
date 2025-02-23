def main():
	total = 0
	while True:
		try:
			food = input('Item? ')
			food = food.lower()
			for item, price in menu.items():
				if item.lower() == food:
					total += price
					print(f'${total:.2f}')
					break
		except EOFError:
			print('')
			print(f'Total: ${total:.2f}')
			break

menu = {
	"Baja Taco": 4.25,
	"Burrito": 7.50,
	"Bowl": 8.50,
	"Nachos": 11.00,
	"Quesadilla": 8.50,
	"Super Burrito": 8.50,
	"Super Quesadilla": 9.50,
	"Taco": 3.00,
	"Tortilla Salad": 8.00
}

main()