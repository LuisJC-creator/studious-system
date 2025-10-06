def triArea(x1, y1, x2, y2, x3, y3):
    component = float(x1)*(float(y2) - float(y3)) + float(x2)*(float(y3)-float(y1)) + float(x3)*(float(y1)-float(y2))
    # this is my solution to absolute value
    if component < 0:
        component * -1
    else:
        component = component
    area = 0.5 * float(component)
    print(f"The area is: {area}")

x1, y1, x2, y2, x3, y3 = input("Please input three points: ").split()
triArea(x1, y1, x2, y2, x3, y3)