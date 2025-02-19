tweet = input('Tweet? ')
for char in tweet:
    if char in 'aeiouAEIOU':
        print('', end='')
    else:
        print(char, end='')

print('')