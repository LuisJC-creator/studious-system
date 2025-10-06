number1, number2, number3 = input("Enter three integer numbers: ").split()
num1 = int(number1)
num2 = int(number2)
num3 = int(number3)
maxNum = 0
minNum = 0
if num1 >= num2 and num1 >= num3: 
    maxNum = num1
    if num2 >= num3:
        minNum = num3
    else:
        minNum = num2
elif num2 >= num1 and num2 >= num3:
    maxNum = num2
    if num1 >= num3:
        minNum = num3
    else:
        minNum = num1
elif num3 >= num1 and num3 >= num2:
    maxNum = num3
    if num1 >= num2:
        minNum = num2
    else:
        minNum = num1
# I'm pretty sure this is un-needed but not 100% on it.
else:
    maxNum = num3
    if num1 >= num2:
        minNum = num2
    else:
        minNum = num1

print("Maximum number is " + str(maxNum))
print("Minimum number is " + str(minNum))
