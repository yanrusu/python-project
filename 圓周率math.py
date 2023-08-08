import math
d=60;r=6
for i in range(15):
    a=d*(math.pi/180)
    y=math.cos(a)
    x=2-2*y
    x = x**0.5
    print(r,y,x,x*(r//2))
    d=d//2
    r*=2
