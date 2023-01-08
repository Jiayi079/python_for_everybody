# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail. The
# program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to
# find the most prolific committer.

# let the user input file name
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

# open file
handle = open(name)

# create a new emply dictionary
dic = dict()

# for loop to read each line in file
for line in handle:
    # remove uneccesary "\n"
    line = line.rstrip()
    # find "From " line to get the email address
    if "From " in line:
        # split whole line to get the email address
        words = line.split()
        # check email address already in "dic" or not, and get the values
        x = dic.get(words[1], 0) + 1
        # update the new value
        dic[words[1]] = x

# initialize two empty variables
bigKey = None
bigValue = None

# for loop to get the key and the value for the "dic"
for key,value in dic.items():
    # check if the value is bigger than the biggest value we get
    if bigValue is None or bigValue < value:
        bigKey = key
        bigValue = value

# print out the result
print(bigKey, bigValue)
