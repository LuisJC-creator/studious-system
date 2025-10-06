L1, L2, L3 = input("Please input the lengths of three line segments: ").split()
if(float(L1) <= 0 or float(L2) <= 0 or float(L3) <= 0):
    print("Zero and negative numbers not allowed, please try again.")
else:
    sum1 = float(L1) + float(L2)
    sum2 = float(L2) + float(L3)
    sum3 = float(L1) + float(L3)
    triangle1 = sum1 > float(L3)
    traingle2 = sum2 > float(L1)
    triangle3 = sum3 > float(L2)
    if triangle1 and traingle2 and triangle3:
        print("Yes")
    else:
        print("No")