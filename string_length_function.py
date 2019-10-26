def string_length(str):
    if type(str) == int or type(str) == float:
        return("Sorry, cannot compute length of numbers.")
    else:
        return len(str)


print(string_length(3.5))
