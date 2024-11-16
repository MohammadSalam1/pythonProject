#we will use calculatoins so best to import math library
#comment whichever is the non desired calc
import math

#calculate the area of a circle
#radian_of_circle = float(input("whats the radian for the circle? "))
#area_of_circle = 2 * math.pi * radian_of_circle**2

#print(f"the area of the circle rounded up to two decimals {area_of_circle:.2f}")

#calculate the radien of the circle
area = float(input("what is the area of the cirlce? "))

#the formulat to calculate the radien
radian = math.sqrt(area/math.pi)

print(f"the radian rounded up to two decimals is: {radian:.2f}")