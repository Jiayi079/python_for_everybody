# Write a program that prompts for a file name, then opens that file and reads
# through the file, looking for lines of the form:
#
# X-DSPAM-Confidence:    0.8475
#
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

# initial two vairables used to get the average
total = 0
count = 0

# for loop to read each line of the file
for line in fh:
    # find the line which is starting with "X-DSPAM-Confidence:"
    if not line.startswith("X-DSPAM-Confidence:"):
        # if not find the line we are looking for, jump to the beginning of the
        # for loop and looking for next line again
        continue

    # everything below in the for loop will run if only if this line is starting
    # with "X-DSPAM-Confidence:"
    # GOAL: we need get the number at the end of the line
    # and there is a ':' in these lines
    # we need to find the ':' and get the index of it by ysing find() function
    index = line.find(':')
    # get all of the string behind ':'
    new_line = line[index + 1:]
    # convert new_line become float to calculate succesfully
    # add each new_line into total
    total = total + float(new_line)
    # count the total times for these nunber appears
    count = count + 1

# outside of the loop, which means we've already calculate everything in the
# file, and then, we can calculate the average for them
average = total / count

print("Average spam confidence:", average)
