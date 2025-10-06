# Lab instructions ask for input validation, I asked Dr. Kim in class and he said to assume a smart user.
# I'll just follow the lab instructions though.

# We have not covered this in class, but I found the is_a? python equivalent isdigit()
# found here https://www.geeksforgeeks.org/python/python-string-isdigit-method/


while True:
    userNum = input("Input an integer: ")
    if userNum.isdigit() and int(userNum) > 0:
        num = int(userNum)
        break

    else:
        print("Invalid input: ")

count = 0
testNum = 2

while count != num:
    prime = True
    # checking if prime
    for i in range(2, testNum):
        if testNum % i == 0:
            prime = False
            break

    if prime:
        print(testNum, end=" ")
        count += 1

    testNum += 1