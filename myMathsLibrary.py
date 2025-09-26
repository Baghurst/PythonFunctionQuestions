import math
#---AREA OF CIRCLE---
def circle_area(diameter):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

#---CIRCUMFERENCE OF CIRCLE---
def circle_perim(radius):
    circumference = radius * math.pi * 2
    return circumference

#---AREA OF RECTANGLE---
def rectangle_area(h,w): #h = Height, w = Width
    area = h * w
    return area

#---PERIM OF A RECTANGLE---
def rectangle_perim(h,w): #h = Height, w = Width
    perim = (h + w) * 2
    return perim