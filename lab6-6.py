x1, y1 = input("Please enter the first endpoint: ").split()
x2, y2 = input("Please enter the second endpoint: ").split()
x_calc = (float(x2) - float(x1))**2
y_calc = (float(y2) - float(y1))**2
length = (x_calc + y_calc) ** 0.5
print(length)
