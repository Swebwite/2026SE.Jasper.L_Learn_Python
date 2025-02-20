import random

def main():
    name = input('Name? ')
    pchoice = playerchoice()
    ochoice = opponentchoice()
    print(f'{name} chose {pchoice}')
    print(f'opponent chose {ochoice}')
    print(f'you {rungame(pchoice, ochoice)}')



def playerchoice():
    while True:
        pchoice = input('1 = Rock, 2 = paper, or 3 = scissors? ')
        if pchoice in ['1', '2', '3']:
            return int(pchoice)
        else:
            print('Please enter 1, 2, or 3 ')

def opponentchoice():
    ochoice = random.randint(1, 3)
    return int(ochoice)

def rungame(pchoice, ochoice):
    if ochoice - pchoice == -1 or ochoice - pchoice == 2:
        return 'win!'
    elif ochoice == pchoice:
        return 'tied!'
    else:
        return 'lose!'



main()