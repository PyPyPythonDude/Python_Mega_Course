'''
This program imports the datetime class of the datetime module and the
installed package, glob2.
Using glob2.glob method, it grabs all .txt files and stores them in a variable.
It then opens a brand new txt file and names it with the current date, using
the datetime module. It uses Python's strftime directives to format the
datetime object into a string. Within the main with statement, the program
iterates through the txt files that were stored in the variable at the
beginning. It opens each of the txt files in read mode, and writes all the
contents of each into the main file that is named after the current date.
'''

from datetime import datetime as dt
import glob2

filenames = glob2.glob("*.txt")

with open(dt.now().strftime("%Y-%m-%d-%H-%M-%S")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename, 'r') as f:
            file.write(f.read()+"\n")
