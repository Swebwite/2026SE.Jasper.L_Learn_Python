def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")


def is_valid(s):
	if len(s) > 6 or len(s) < 2:
		return False
	if not s[0].isalpha() or not s[1].isalpha():
		return False
	for char in s:
		if not (char.isalpha() or char.isdigit()):
			return False
	number_found = False
	for char in s:
		if char.isdigit():
			number_found = True
		if number_found and char.isalpha():
			return False
	y = 0
	for i, char in enumerate(s):
		if char.isalpha():
			y += 1
		elif char.isdigit():
			if i == y and char == '0':
				return False
	return True

main()