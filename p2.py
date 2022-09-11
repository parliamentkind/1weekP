import math

x = int (input('Enter x value: '))
t = int (input('Enter t value: '))
a = (9*math.pi*t)+(10*math.cos(x))
b = (math.sqrt(t)-math.fabs(math.sin(t)))
z = (a/b*math.pow(math.e,x))
print(z)