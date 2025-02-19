def main():
	text = input('Text? ')
	for char in text:
		if char != char.lower():
			print('_', end='')
		print(char.lower(), end='')

main()

print('\n')