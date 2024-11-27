print("""Task1. "Temperature Converter"
Write a Python program that prompts the user to enter a temperature in Celsius and then
converts it to Fahrenheit using the formula: F = (C * 9/5) + 32. Your program should then
print out the converted temperature in Fahrenheit.
However, if the user enters a temperature below -273.15°C (the lowest possible
temperature in the universe, also known as absolute zero), your program should print an
error message instead of attempting to convert the temperature.
Note: You can assume that the user will enter a valid input (a number for the temperature in Celsius).
Example output:
Enter the temperature in Celsius: 25
25°C is equivalent to 77°F
Example output (if the user enters a temperature below absolute zero):
Enter the temperature in Celsius: -300
Error: Temperature below absolute zero (-273.15°C)

""")

temperature=(input("Enter a temperature in Celsius: "))
temp_float = round(float(temperature),2) if temperature.replace(".","",1).replace("-","",1).isdigit() and len(temperature) >= 1 else None
if not temp_float:
    raise Exception("Value that you entered is not a number")
  
temp_fareng: float=round(temp_float * 9 / 5 + 32, 2)

if temp_float < -273.15:
    print("Temperature below absolute zero (-273.15°C)")
else:
    print(f"{temp_float}°C is equivalent to {temp_fareng}°F")