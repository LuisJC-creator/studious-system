num = input("Please input a number? ")
print("Processing...")
if(float(num) > 0):
    print(num + " is a positive number.")
elif(float(num) < 0):
    print(num + " is a negative nubmer.")
else:
    print(num + " is zero.")