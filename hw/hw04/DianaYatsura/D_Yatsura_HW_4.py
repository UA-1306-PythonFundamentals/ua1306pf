def converter_temperature():
    temperature_in_c = round(float(input('Please, enter the temperature in Celsius: ')),  2)
    temperature_in_f = round(float((temperature_in_c * 9 / 5) + 32), 2)
    if temperature_in_c < -273.15:
        print('Error: Temperature below absolute zero (-273.15℃)')
    else:
        print(str(temperature_in_c) + chr(176) + "C", "is equivalent to", str(temperature_in_f)
              + chr(176) + "F")

converter_temperature()