temperatures=[10,-20,-289,100]
#this function will take 2 parameters: the list of temps, and the filepath
def celcius_to_fahrenheit(temperatures, filepath):
    #within our function, we are opening a file in write mode
    with open(filepath, "w") as file:
        for c in temperatures:
            #check if condition is met
            if c > -273.15:
                #calculate celcius to fahrenheit conversion
                f = c * 9/5 + 32
                #write each result to a new line in the text file
                file.write(str(f)+"\n")

#call the function
celcius_to_fahrenheit(temperatures, "temperatures.txt")
