import numpy as np  

fahrenheit = np.array([12.5, 37.8, 45.2, 59.9, 68.4, 77.7, 101.3, 150.5, 180.6, 200.0])

celsius = (fahrenheit - 32) * 5.0 / 9.0

print("Fahrenheit:")
print(fahrenheit)

print("Celsius:")
print(celsius)
