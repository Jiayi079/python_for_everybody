# 8.4 Open the file romeo.txt and read it line by line. For each line, split the
# line into a list of words using the split() method. The program should build a
# list of words. For each word on each line check to see if the word is already
# in the list and if not append it to the list. When the program completes, sort
# and print the resulting words in python sort() order as shown in the desired
# output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

# let the user input the file name
fname = input("Enter file name: ")

# check if the file can be opened
try:
    fh = open(fname)
except:
    print("Can't open file: ", fname)
    quit()

# initialized a new empty list
lst = list()

# for loop to get each line in the file
for line in fh:
    # delete the unnecessary "\n"
    words = line.rstrip()
    # split each words in line by space to become a new list
    list = words.split()
    # for loop to check each words in the list
    for w in list:
        # if the words doesn't contain in the "lst"
        if w not in lst:
            # add it into "lst"
            lst.append(w)
# sort words in lst
lst.sort()
print(lst)
