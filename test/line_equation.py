def angel_coef(x1, y1, x2, y2):
    m = 0
    if y2 - y1 != 0 and x2 - x1 != 0:
        m = (y2-y1) / (x2 - x1)
    return m
    
def coef_c(x, y, m):
    c = -m * x + y
    
    return c

def intersection(a1x, a1y, b1x, b1y, a2x, a2y, b2x, b2y):
    m1 = angel_coef(a1x, a1y, b1x, b1y)
    m2 = angel_coef(a2x, a2y, b2x, b2y)

    c1 = coef_c(a1x, a1y, m1)
    c2 = coef_c(a2x, a2y, m2)

    print('y = ' + str(m1) + 'x + ' + str(c1))
    print('y = ' + str(m2) + 'x + ' + str(c2))

    print(str(c2 - c1) + ' ' + str(m1 - m2))
    x = 0

    if m1 == 0 and m2 == 0:
        if a1x == b1x and a2y == b2y:
            x = a1x
            y = a2y
        elif a1y == b1y and a2x == b2x:
            x = a2x
            y = a1y
        else:
            print('параллельны')
            x = 0
            y = 0
    elif m1 == 0:
        if a1x == b1x:
            x = a1x
            y = m2 * x + c2
        else:
            y = a1y
            x = (y - c2) / m2
    elif m2 == 0:
        if a2x == b2x:
            x = a2x
            y = m1 * x + c1
        else:
            y = a2y
            x = (y - c1) / m1
    else:
        x = (c2 - c1) / (m1 - m2)
        y = m1 * x + c1

    return [x, y]

def parse_command(command):
    index
    for letter in command:
        if letter == 'X':
            flagx = True
            xb = index
            break
        index += 1
    for j in range(xb + 1, len(command)):
        if command[j].isdigit() or command[j] == '.':
            index += 1
            if j + 1 == len(command):
                xe = index
        else:
            xe = index
            break

    if flagx:
        x = float(command[xb + 1:xe + 1])
        

    index = 0
    for letter in command:
        if letter == 'Y':
            flagy = True
            yb = index
            break
        index += 1
    for j in range(yb + 1, len(command)):
        if command[j].isdigit() or command[j] == '.':
            index += 1
            if j + 1 == len(command):
                ye = index
        else:
            ye = index
            break

    if flagy:
        y = float(command[yb + 1:ye + 1])

    return ans
    

a1x, a1y, b1x, b1y, a3x, a3y, b3x, b3y = 457.240, 2231.185, 1758.158, 2104.716, 1758.158, 1921.517, 457.240, 1795.204
a2x, a2y, b2x, b2y = 1866.498, 1877.161, 1866.498, 2149.641
ans = intersection(a1x, a1y, b1x, b1y, a2x, a2y, b2x, b2y)
ans2 = intersection(a3x, a3y, b3x, b3y, a2x, a2y, b2x, b2y)
print('G0X' + "{:.3f}".format(ans[0]) + 'Y' + "{:.3f}".format(ans[1]))
print('G1Z-10.200F1500.0')
if a1x > b1x:
    print('G1X' + str(a1x) + 'Y' + str(a1y) + 'F3500.0')
else:
    print('G1X' + str(b1x) + 'Y' + str(b1y) + 'F3500.0')
print('G0Z15.000')
print('G0X' + "{:.3f}".format(ans2[0]) + 'Y' + "{:.3f}".format(ans2[1]))
print('G1Z-10.200F1500.0')
if a3x > b3x:
    print('G1X' + str(a3x) + 'Y' + str(a3y) + 'F3500.0')
else:
    print('G1X' + str(b3x) + 'Y' + str(b3y) + 'F3500.0')
print('G0Z15.000')
