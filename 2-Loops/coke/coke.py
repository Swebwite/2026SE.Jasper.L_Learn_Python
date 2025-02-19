x = 50

while x > 0:
    y = int(input(f"Amount due: {x} "))
    if y == 25:
        x = x - y
    if y == 10:
        x = x - y
    if y == 5:
        x = x - y
while x < 0:
    x = x * -1
    print(f"Change: {x}")
if x == 0:
    print("Enjoy your coke!")