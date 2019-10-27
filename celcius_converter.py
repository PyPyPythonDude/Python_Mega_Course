#This function will take in a temperature in Celcius degrees, and convert it to Fahrenheit
def celcius_to_fahrenheit(c):
    if c > -273.15:
        f = c * 9/5 + 32
        return f
    else:
        #the lowest possible temperature that physical matter can reach is -273.15C
        return "Cannot compute. The lowest possible temperature is -273.15C."


temperatures = [10,-20,-289,100]
for temp in temperatures:
    print(celcius_to_fahrenheit(temp))
