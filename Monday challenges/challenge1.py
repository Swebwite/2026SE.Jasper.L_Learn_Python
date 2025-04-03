L1 = [ 'p', 'n', 't', 'y', 'x', 'j' ]
L2 = [ '4', '9', '0', '3', '3', '7' ]

L1.sort()
L2.sort()
print(L1, L2)

def table():
    print('| Col 1 | Col 2 |')
    print('|-------|-------|')
    i = 0
    for a in L1:
        print(f'|   {a}   |   {L2[i]}   |')
        i += 1

def txtdoc():
    file1 = open('L1.txt', 'w')
    file2 = open('L2.txt', 'w')
    for i in L1:
        file1.write(f'{i}\n')
    file1.close()
    for i in L2:
        file2.write(f'{i}\n')
    file2.close()

def main():
    table()
    search = int(input('row 1-6? '))
    search -= 1
    print(f'letter: {L1[search]}\nnumber: {L2[search]}')
    txtdoc()

main()