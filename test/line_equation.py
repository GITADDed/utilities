def angel_coef(x1, y1, x2, y2):
    return (y2-y1) / (x2 - x1)
    
def coef_c(x, y, m):
    c = -m * x + y
    
    return c

def intersection(a1x, a1y, b1x, b1y, a2x, a2y, b2x, b2y):
    m1 = angel_coef(a1x, a1y, b1x, b1y)
    m2 = angel_coef(a2x, a2y, b2x, b2y)

    c1 = coef_c(a1x, a1y, m1)
    c2 = coef_c(a2x, a2y, m2)

    y = m1x1 + c1
    y = m2x2 + c2
    m1x + c1 = m2x + c2
    m1x - m2x = c2 - c1
    x = c2 - c1 / m1 - m2

    return []
