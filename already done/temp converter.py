print("Input the current tempurature.")
temp = float(input())
print("input a valid system of measurement. use the full word (ex. 'Celcius' instead of 'C').")
meas = str(input())
meas = meas.lower
if (meas == ("fahrenheit")) or (meas == ("farenheit")):
    F = temp
    C = (F - 32) * (5/9)
    K = C + 273.15
    print(f"Your tempurature in Fahrenheit is {F}, in Celcius it's {C}, and in Kelvin it's {K}.")
elif (meas == ("celcius")):
    C = temp
    F = (C + 32) * (9/5)
    K = C + 273.15
    print(f"Your tempurature in Fahrenheit is {F}, in Celcius it's {C}, and in Kelvin it's {K}.")
elif (meas == ("kelvin")):
    K = temp
    C = K - 273.15
    F = (C + 32) * (9/5)
    print(f"Your tempurature in Fahrenheit is {F}, in Celcius it's {C}, and in Kelvin it's {K}.")
else:
    print("you have not entered a valid system of measurement. valid systems of measurement are Fahrenheit, Celcius, and Kelvin. please try again")
