glist = {}

def main():
    while True:
        try:
            item = input('item? ')
            if item in glist:
                glist[item] += 1
            else:
                glist[item] = 1
        except EOFError:
            print()
            printlist(glist)
            break

def printlist(dct):
    sorted_dct = sortlist(dct)
    for key, value in sorted_dct.items():
        print(f"{key}: {value}")

def sortlist(dct):
    return dict(sorted(dct.items(), key = lambda item: item[0].lower()))

main()