#5
print("NUM 5")

import math
import myMathsLibrary

#---FUNCTIONS---


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
    result = myMathsLibrary.circle_area(radius)
    print(f"The area of the circle is {result}")

#---CIRC OF A CIRCLE---
elif options == 2:
    radius = float(input("Enter the radius of the circle: "))
    result = myMathsLibrary.circle_perim(radius)
    print(f"The circumference of the circle is {result}")

#---AREA OF A RECTANGLE---
elif options == 3:
    h = float(input("Enter the height of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    rectangle_area = myMathsLibrary.rectangle_area
    print(f"The Area of the square is {rectangle_area(h,w)}")
    
#---PERIM OF A RECTANGLE---

elif options == 4:
    h = float(input("Enter the height of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    rectangle_perim = myMathsLibrary.rectangle_perim
    print(f"The Perimeter of the square is {rectangle_perim(h,w)}")

