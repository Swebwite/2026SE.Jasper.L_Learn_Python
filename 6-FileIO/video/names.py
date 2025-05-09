'''
names = []

for _ in range(3):
    names.append(input('Whats your name? '))

for name in sorted(names):
    print(f'hello, {name}')
'''
'''
name = input('Whats your name? ')

with open('names.txt', 'a') as file:
    file.write(f'{name}\n')
'''
'''
with open('names.txt', 'r') as file:
    for line in file:
        print('hello,', line.rstrip())'
'''

names = []

with open('names.txt') as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f'hello, {name}')