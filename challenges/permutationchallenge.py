mynum = [1, 2, 3]

for x in mynum:
    for y in mynum:
        if y != x:
            for z in mynum:
                if z != x and z!= y:
                    print(x, y, z)