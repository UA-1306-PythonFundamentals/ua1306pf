celsius_temp = float(input("Enter temperature in Celsius: "))

if celsius_temp < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    print(f"{celsius_temp}°C is equivalent to {fahrenheit_temp}°F")
