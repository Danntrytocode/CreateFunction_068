##Create a function that converts temperature from Celsius to Fahrenheit and vice versa. 
##The function accepts two parameters, namely the temperature value and the temperature unit ('C' for Celsius, 'F' for Fahrenheit).
def converts_temp(value, unit):
    if unit == 'C':
        return (value * 9/5) + 32 #dengan validasi: elif value == "F".. return value.. else: print("Unit harus 'C' atau 'F'")
    else:
        print("Unit nya 'C' Masseh")
