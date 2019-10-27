#open a file in read-mode
file = open("fruits.txt", 'r')
#read the contents of the file line by line
content = file.readlines()
#close the file when you no longer need to read from it
file.close()
#loop through the lines
for line in content:
    #use the strip() method so you don't print any newline (\n) characters
    print(len(line.strip()))
