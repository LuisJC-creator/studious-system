g1, g2, g3 = input("Enter your grades (e.g., A B C): ").split()
g1 = g1.upper()
g2 = g2.upper()
g3 = g3.upper()

# I wanted to make these inputs into a list of grades [g1, g2, g3] and loop through with for
# but I figured that was outside of the scope of this lab, so I'm sorry in advance
# for the rest of this code.

if g1 == "A":
    first = 4.0
elif g1 == "B":
    first = 3.0
elif g1 == "C":
    first = 2.0
elif g1 == "D":
    first = 1.0
elif g1 == "F":
    first = 0.0
else:
    print("Error, incorrect input")
    
if g2 == "A":
    second = 4.0
elif g2 == "B":
    second = 3.0
elif g2 == "C":
    second = 2.0
elif g2 == "D":
    second = 1.0
elif g2 == "F":
    second = 0.0
else:
    print("Error, incorrect input")

if g3 == "A":
    third = 4.0
elif g3 == "B":
    third = 3.0
elif g3 == "C":
    third = 2.0
elif g3 == "D":
    third = 1.0
elif g3 == "F":
    third = 0.0
else:
    print("Error, incorrect input")

avg = (first + second + third) / 3
print("Your GPA is: " + str(avg))

