from serious import is_inside
point = [100, 120]
rectangle = [140, 60, 100, 200]
if is_inside(point, rectangle) == False:
    print ("Your function is correct")
else:
    print ("Your function got a bug")