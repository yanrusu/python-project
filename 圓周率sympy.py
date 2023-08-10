import math
from sympy import *
n=60 ;y=6
print('邊 ','cos','              邊長     ','      邊長 * 2/n')
for i in range(15):
    a=math.radians(n)
    x=cos(a)
    z = 2-2*x
    z = z **0.5
    print(y,cos(a),z,z*(y/2),sep=" ")
    print()

    n=n/2
    y*=2



