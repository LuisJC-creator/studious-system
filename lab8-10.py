import math
# imported math for the angle cos / acos stuff
# value of pi from cylinder assignment
pi = 3.142592
x, y = input("Please enter the origin on the circle (x, y) ").split()
x = float(x)
y = float(y)
r = input("Please enter the radius of the circle ")
r = float(r)
x1, y1, x2, y2 = input("Please enter the two points on a line (x1, y1, x2, y2) ").split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

# line vector length
deltaX = x2 - x1
deltaY = y2 - y1

lineLength = (deltaX**2 + deltaY**2)**0.5

# distance from circle center to line
num = deltaX*(y1 - y) - deltaY*(x1 - x)
distCirc = (num*num)**0.5 / lineLength

# Segment = Sector - triangle
if distCirc >= r:
    smallSeg = 0.0
else:
    # full and half mean angles
    half = math.acos(distCirc / r)
    full = 2 * half
    sector = 0.5 * r * r * full
    triangle = distCirc * (r*r - distCirc*distCirc)**0.5
    smallSeg = sector - triangle

largeSeg = pi * r * r - smallSeg
print(largeSeg)