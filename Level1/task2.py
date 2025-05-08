def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

def temp_converter():
    temp=float(input('Enter Temperatue:'))
    unit=input('enter units(C for Celsius,F for fahrenheit):').upper()

    if unit=='C':
        convert=celsius_to_fahrenheit(temp)
        print(f"The fahrenheit is:{convert}F")
    elif unit=='F':
        convert= fahrenheit_to_celsius(temp)
        print(f"The celsius is:{convert}C")
    else:
        print("Invalid units.")

temp_converter()