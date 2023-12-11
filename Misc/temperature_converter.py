"""
Simple Temperature Converter 
Input:
    -- Temperature
    -- Scale of the temperature
Output:
    -- The converted temperature either to Celsius or Fahrenheit  
"""
while True:
    try: 
        user_temperature = float(input("Enter the temperature: "))
        break
    except:
        ValueError
        print("Numbers are only allowed.")
while True:
    scale = input("What is the scale of this temperature (C, F): ")
    if scale.lower() == 'c' or scale.lower() == 'f':
        break
    print("Enter valid scale.")

if scale.lower() == 'c':
    converted_temp = round((user_temperature * 9/5) + 32, 2)
    print(f"Converted temperature {converted_temp} F.")
else:
    converted_temp = round((user_temperature - 32) * 5/9, 2)
    print(f"Converted temperature {converted_temp} C.")