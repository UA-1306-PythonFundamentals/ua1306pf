def celsius_to_fahrenheit(degree):
    absolute_zero = -273.15
    fahrenheit = (degree * 9 / 5) + 32

    if degree < absolute_zero:
        return f"Error: Temperature below absolute zero ({absolute_zero}°C)"
    else:
        return f"{degree}°C is equivalent to {fahrenheit:.1f}°F"


try:
    celsius = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(celsius)
    print(result)
except ValueError:
    print("Invalid input. Please enter a numerical value for Celsius.")
