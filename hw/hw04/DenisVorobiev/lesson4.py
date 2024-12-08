print("Enter the temperature in Celsius: ")
C = float(input ("temperature :"))
if C < - 273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    F = (C * 9 / 5) + 32
    print("temperature", F)
