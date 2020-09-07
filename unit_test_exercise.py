def line_maker(p1, p2, x):
    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p2[1] - (slope*p2[0])
    y = (slope*x) + b
    return y

def point_tester(p1, p2, p3):
    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p2[1] - (slope*p2[0])
    y = (slope*p3[0]) + b
    if y == p3[1]:
        return True
    else:
        return False
