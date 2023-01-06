# 7.1 Write a program that prompts for a file name, then opens that file and
# reads through the file, and print the contents of the file in upper case. Use
# the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name

# let the user input file name and named "fname"
fname = input("Enter file name: ")

# try-except open "fname" file
try:
    fh = open(fname)
except:
    # except will run if only if "fname" can not be opened
    print("Can't open file: ", fname)
    quit()  # exit the program if can't open file

# for loop to read each line in file
for line in fh:
    # remove \n at the end of each line
    line = line.rstrip()
    # print out the result by using upper() function to let everything is uppercase
    print(line.upper())
