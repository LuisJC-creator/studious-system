# question, when I tried to typecast float(input("please input three points ")).split() or putting .split() inside
# parenthesis, I got an error, why? 
# The following implementation worked, but it is ugly.
x1, y1, x2, y2, x3, y3 = input("Please input three points ").split()
triArea = ((float(x1) * (float(y2) - float(y3)) + float(x2) * (float(y3) - float(y1)) + float(x3) * (float(y1) - float(y2)))) * 0.5
print("The area is " + str(triArea))
