temp_input = input("Enter the temperature in Celsius: ")

if temp_input.replace('.', '', 1).replace('-', '', 1).isdigit():
    temp_celsius = float(temp_input)
    if temp_celsius > -273.15:
        temp_fahrenheit = round((temp_celsius * 9 / 5) + 32, 2)
        print(f"{temp_celsius} °C is equivalent to {temp_fahrenheit} °F")
    else:
        print(f"Error: Temperature below absolute zero ({temp_celsius} °C)")
else:
    print("Error: Not a valid number")

