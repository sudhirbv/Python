import math
def area(r):
    if(type(r) == str):
        print("Enter either a integer or float:")
    else:
        PI=3.14
        Area=(PI * r * r)
        print("Area of the circle is: ",Area)

radius=int(input("Enter the Radius value:"))
area(radius)


#Sample output:
#Enter the Radius value:6
#Area of the circle is:  113.03999999999999   
