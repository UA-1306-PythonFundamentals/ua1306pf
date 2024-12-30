temp = float(input("Enter the temperature in Celsius: "))

if temp >= -273.15:
    tempInFahr = (temp * (9/5)) + 32
    print(f"{temp}°C is equivalent to {tempInFahr}°F")
else :
    print("Error:Temperature below absolute zero (-273.15)")
