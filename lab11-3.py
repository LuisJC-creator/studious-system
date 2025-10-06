def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

uNum = int(input("Please input an integer: "))
if prime(uNum):
    print(f"{uNum} is a prime number")
else:
    print(f"{uNum} is not a prime number")