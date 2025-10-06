num = int(input("Please enter a number "))
for i in range(num):
    for j in range(1, num-i):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
            
    print()