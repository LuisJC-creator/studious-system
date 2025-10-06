numTests = int(input("Please enter the number of test cases. "))
cases = []
for i in range(numTests):
    priceCookie, numCookie, amtMoney = input("Enter price of cookies, number of cookies, and the amount of money. ").split()

    priceCookie = float(priceCookie)
    numCookie = int(numCookie)
    amtMoney = float(amtMoney)

    cases.append((priceCookie, numCookie, amtMoney))

for ele in cases:
    # I used ele to go through array
    # 0 is price of each, 1 is number of cookies to buy, 2 is how much money we have (for my reference while making)
    askAmt = (ele[0] * ele[1]) - ele[2]
    if askAmt < 0:
        print(0.00)
    else:
        print(askAmt)