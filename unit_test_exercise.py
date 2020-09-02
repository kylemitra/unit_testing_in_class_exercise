def line_maker(x1, y1, x2, y2, x):
    slope = (y2-y1) / (x2-x1)
    b = y2 - (slope*x2)
    y = (slope*x) + b
    return y

def point_tester(x1, y1, x2, y2, x3, y3):
    slope = (y2-y1) / (x2-x1)
    b = y2 - (slope*x2)
    y = (slope*x3) + b
    if y == y3:
        return True
    else:
        return False
