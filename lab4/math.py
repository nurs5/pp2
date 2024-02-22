import math 
deg=int(input("Input degree:"))
rad=math.radians(deg)
print(f"Output radian: {rad}")
#ex1
hei=int(input('Height: '))
base1=int(input('Base, first value:'))
base2=int(input('Base, second value:'))
c=(base1+base2)/2*hei
print(f"Expected Output: {c}")
#ex2
sides=int(input('Input number of sides: '))
len=int(input('Input the length of a side: '))
area=(sides*(len**2))/(4*math.tan(math.pi/sides))
print(f"The area of the polygon is: {round(area)}")
#ex3
base=int(input("Length of base: "))
hei=int(input("Heigh of parallelogram: "))
area=float(base*hei)
print(f"Expected Output: {area}")  
##ex 4
