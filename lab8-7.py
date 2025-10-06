s1, s2, s3, s4 = input("Please enter four integer sides: ").split()
print("Input: " + s1 + " " + s2 + " " + s3 + " " + s4)
if(int(s1) <= 0 or int(s2) <= 0 or int(s3) <= 0 or int(s4) <= 0):
    # No negative sides or no sides that are 0.
    print("Input cannot be negative or 0")
else:
    if int(s1) == int(s2) and int(s3) == int(s4):
        print("YES")
    elif int(s1) == int(s3) and int(s2) == int(s4):
        print("YES")
    elif int(s1) == int(s4) and int(s2) == int(s3):
        print("YES")
    else:
        print("NO")
    