C = float(input('Enter the temperature in Celsius:'))

if C < -273.15:
        print('Error: Temperature below absolute zero (-273.15 C)')
else:
        F = (C * 9/5) + 32
        print(f'{C}C is equivalent to {F:.2f}F')