#    This program is to count instances of particular values or names in a file.
#    It requires two inputs at the command line, the first is the file being read, and the second
#    is the file to be written with the keys and values in a csv file.
#    Written by Robert Tyx wyu3@cdc.gov on 3/3/2014
#    File: instance_counter.py

import csv  # Comma Separated variable module
import sys  # system module

def count_names(lines):  # function for counting names using lines as input
    result = {}   # create library called result
    for name in lines:  # at every new line, do the following
        name = name.strip()  # strip off any spaces etc
        if name in result:   # if the name key of what we are counting is in the library already
            result[name] = result[name]+1  # add one to the name key
        else:   # otherwise do the following
            result[name] = 1  # add the name key and one to the library
    return result   # return the library to what called the function

if __name__ == '__main__':   
    reader = open(sys.argv[1],'r')  # open file specified by command line
    lines = reader.readlines()  # read each line into lines
    reader.close()
count = count_names(lines)  # call function count_names
for name in count:  # print out all keys and values onto screen 
    print name, count[name]
writer = csv.writer(open(sys.argv[2], 'wb'))  # write to the second file specified in command line
for key, value in count.items():  # write each key and value 
        writer.writerow([key,value])
