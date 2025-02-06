# Ask user for their name
name = input("What's your name? ").strip().title()

# Split the users first and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")