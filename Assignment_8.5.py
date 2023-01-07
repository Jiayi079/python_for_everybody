# Open the file mbox-short.txt and read it line by line. When you find a line
# that starts with 'From ' like the following line:
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# You will parse the From line using split() and print out the second word in
# the line (i.e. the entire address of the person who sent the message). Then
# print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at
# the last line of the sample output to see how to print the count.
#
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# let the user input file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

# open the file
fh = open(fname)
count = 0   # initial count to calculate the appears time

# for loop to read each line in the text file
for line in fh:
    # check if "From " doesn't contain in this line, skip to next line
    if "From " not in line:
        continue
    # next part (line 28 - line 31) will run if only if "From " contains in line
    count = count + 1   # calculate the count time, increment by one
    list = line.split() # split each variables by space
    print(list[1])  # print out the second varaible in the list, which is email

print("There were", count, "lines in the file with From as the first word")
