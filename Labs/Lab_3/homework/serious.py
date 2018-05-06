def remove_dollar_sign(s):
    s = s.replace("$", "")
    return s

def get_even_list(l):
    for i in l:
        if abs(i) % 2 == 1:
            l.remove(i)
    return l

def is_inside(point, rectangle):
    x = point[0]
    y = point[1]
    x1 = rectangle[0]
    y1 = rectangle[1]
    width = rectangle[2]
    length = rectangle[3]
    if x1 < x < x1 + width and y1 < y < y1 + length:
        return True
    else:
        return False