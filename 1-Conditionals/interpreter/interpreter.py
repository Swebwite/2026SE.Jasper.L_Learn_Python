eq = input('equation? ')
x, y, z = eq.split(' ')

if y.find('+') != -1:
    print(round(float(x) + float(z), 1))
if y.find('-') != -1:
    print(round(float(x) - float(z), 1))
if y.find('/') != -1:
    print(round(float(x) / float(z), 1))
if y.find('*') != -1:
    print(round(float(x) * float(z), 1))