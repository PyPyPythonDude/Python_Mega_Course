#Create a new txt file in write mode
file = open("example2.txt", "w")
#create a list
numbers = [1, 2, 3]
#write each item in list into a new line in the open text file
#note: must convert number to string as write method can only take strings
for number in numbers:
    file.write(str(number)+"\n")
#close the text file
file.close()
