num = int(input("Please enter a number "))
for i in range(num):
    for j in range(num-i):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
            
    print()