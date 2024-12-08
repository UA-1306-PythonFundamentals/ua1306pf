celsius = float(input('Write you tempreture'))

if celsius <273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C is equivalent to {fahrenheit}°F")