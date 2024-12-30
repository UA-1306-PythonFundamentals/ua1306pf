# Введення температури та заміна коми на крапку, якщо необхідно
temp_input=input("Enter the temperature in Celsius:")
temp_input = temp_input.replace(",", ".")
# Позначаю додаткові перемінні
f1=0
f2=0
# Випадок коли число з крапкою
if temp_input.count(".")==1:
    f1=1
    if temp_input.replace(".","").isdigit:
        if float(temp_input) <= -273.15:
            print("Error: Temperature below absolute zero (-273.15°C)")
        else:
            temp_fahrenheit=(float(temp_input)*(9/5))+32
            print(temp_input, "°C is equvalent to ", temp_fahrenheit, "°F")
# Випадок коли число ціле
if temp_input.count(".")==0 and temp_input.isdigit:
    f2=1
    if int(temp_input) <= -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
    elif int(temp_input):
        temp_fahrenheit=(int(temp_input)*(9/5))+32
        print(temp_input, "°C is equvalent to ", temp_fahrenheit, "°F")
# Всі решта випадків
if f1==0 and f2==0:
    print("Please, only real numbers")