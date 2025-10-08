x = int(input("Enter a number: "))
if x < 0:
    raise Exception(f'x should not be negative. The avlue of x was: {x}')