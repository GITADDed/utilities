def angel_coef(x1, y1, x2, y2):
    return (y2-y1) / (x2 - x1)
    
def line_equation(y, k, b):
    x = (b - y) / k
    return x

def intersection_y_axis_coef(y, x, k):
    return y - k * x
