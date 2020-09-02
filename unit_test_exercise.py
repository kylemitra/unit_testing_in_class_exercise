
def line_maker(x1, y1, x2, y2, x):
    tupletest = (1,2)
    x5, y6 = *tupletest
    slope = (y2-y1) / (x2-x1)
    b = y2 - (slope*x2)
    y = (slope*x) + b
    return y
