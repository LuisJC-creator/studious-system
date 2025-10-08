x = 10
y = 0

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Division by zero!")
else:
    print("Division successful! Result:", result)
finally:
    print("Execution completed.")
