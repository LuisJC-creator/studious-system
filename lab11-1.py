def dollarToPeso(dollarVal):
    pesoVal = dollarVal * 17.1594
    print(f"Mexican Peso: ${pesoVal}" )  


userVal = float(input("US Dollar: $"))
dollarToPeso(userVal)