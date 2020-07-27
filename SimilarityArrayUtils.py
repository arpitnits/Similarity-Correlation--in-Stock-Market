def fix_shape(x, y):
    if x.shape < y.shape:
        y = y[-x.shape[0]:]
    elif x.shape > y.shape:
        x = x[-y.shape[0]:]
    return x, y
