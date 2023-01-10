# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and
# numbers. You will extract all the numbers in the file and compute the sum of
# the numbers.

# Data Files
# We provide two files for this assignment. One is a sample file where we give
# you the sum for your testing and the other is the actual data you need to
# process for the assignment.
# Sample data:
# http://py4e-data.dr-chuck.net/regex_sum_42.txt
# (There are 90 values with a sum=445833)
# Actual data:
# http://py4e-data.dr-chuck.net/regex_sum_1710364.txt
# (There are 69 values and the sum ends with 899)

#These links open in a new window. Make sure to save the file into the same
# folder as you will be writing your Python program. Note: Each student will
# have a distinct data file for the assignment - so only use your own data file
# for analysis.

# Data Format
# The file contains much of the text from the introduction of the textbook
# except that random numbers are inserted throughout the text. Here is a sample
# of the output you might see:
#
# Why should you learn to write programs? 7746
# 12 1929 8827
# Writing programs (or programming) is a very creative
# 7 and rewarding activity.  You can write programs for
# many reasons, ranging from making your living to solving
# 8837 a difficult data analysis problem to having fun to helping 128
# someone else solve a problem.  This book assumes that
# everyone needs to know how to program ...

# Handling The Data
# The basic outline of this problem is to read the file, look for integers using
# the re.findall(), looking for a regular expression of '[0-9]+' and then
# converting the extracted strings to integers and summing up the integers.

# import regrular expression operations
import re

# let the user input file name
file_name = input("Enter file name: ")

# try-except to check if open file succesfully
try:
    open_file = open(file_name)
except:
    print("Failed to open file: ", file_name)
    quit()

sum = 0     # used to sum the total values
count = 0   # used to calculat the total times

# read each line in the file
for line in open_file:
    if re.search('[0-9]+', line):   # search each line if has number
        # findall() function will return all non-overlapping matches of pattern
        # in string, as a list of strings
        lst = re.findall('[0-9]+', line)    # find all numbers in this lines
        # for loop to get each number in the list
        for num in lst:
            sum = sum + int(num)    # calculate the sum values
            count = count + 1       # calculate the total times

print("There are", count,"values with a sum ends with", sum)
