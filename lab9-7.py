num = int(input("Please enter a number "))
for i in range(num):
    for j in range(i+1):
        print(" ", end="")
    # I don't feel that I fully understand this.
    # I had for k in range(1, num-i) before and I was one star off.
    # Is this because it starts at 0?
    for k in range(num-i):
        print("*", end="")
            
    print()