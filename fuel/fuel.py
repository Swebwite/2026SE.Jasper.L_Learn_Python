while True:
    fraction = input('Fuel left? ')
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        fuel = (x / y) * 100
        fuel = round(fuel, 0)
        if 1 < fuel < 99:
            print(f'{fuel:.0f}%')
        if fuel <= 1:
            print('E')
        if fuel >= 99:
            print('F')
        break
    except (ValueError, ZeroDivisionError):
        print('Please enter a valid fraction')