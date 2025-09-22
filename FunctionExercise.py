#1
print("NUM 1")

def prefix(word):
    added = ('un'+word)
    return added
theinput = input("Enter a word: ")
print(prefix(theinput))
    
 #2
print("NUM 2")

def prefix(word):
    added = (word+'s')
    return added
theinput = input("Enter a word: ")
print(prefix(theinput))
        
#3
print("NUM 3")

import math
def circle_area(diameter):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area
diameter = float(input("Enter the diameter of a circle: "))

print(f"The Area of the circle is {circle_area(diameter)}")

#4
print("NUM 4")

import math
def rectangle_area(h,w): #h = Height, w = Width
    area = h * w
    return area
h = float(input("Enter the height of the rectangle: "))
w = float(input("Enter the width of the rectnagle: "))

print(f"The Area of the square is {rectangle_area(h,w)}")

#5
print("NUM 5")

import math

#---FUNCTIONS---

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
#---MAIN PROGRAM---

print("Choose an option:")
print("1. Area of Circle")
print("2. Perimeter of Circle")
print("3. Area of Rectangle")
print("4. Perimeter of Rectangle")

options = int(input("Enter your options (1-4): "))

#---AREA OF A CIRCLE---

if options == 1:
    radius = float(input("Enter the diameter of the circle: "))
    result = circle_area(radius)
    print(f"The area of the circle is {result}")

#---CIRC OF A CIRCLE---
elif options == 2:
    radius = float(input("Enter the radius of the circle: "))
    result = circle_perim(radius)
    print(f"The circumference of the circle is {result}")

#---AREA OF A RECTANGLE---
elif options == 3:
    h = float(input("Enter the height of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    print(f"The Area of the square is {rectangle_area(h,w)}")
    
#---PERIM OF A RECTANGLE---

elif options == 4:
    h = float(input("Enter the height of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    print(f"The Perimeter of the square is {rectangle_perim(h,w)}")
