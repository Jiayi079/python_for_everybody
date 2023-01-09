# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
#
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
#Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

# input file name
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

# open file
handle = open(name)

# create new dictionary -> not allowed duplicates items with same keys
# used dict() to count things
counts = dict()

# create a new list -> defined order which can not be changed
# used to sort the item from dict
lst = list()

# for loop to read each line
for line in handle:
    if "From " in line:     # find "From " line
        time = line.split()
        hour = time[5].split(":")   # get hour
        counts[hour[0]] = counts.get(hour[0], 0 ) + 1   # count hour in dict

# append each items in dict to list
for k,v in counts.items():
    lst.append((k, v))

# sort list
lst.sort()

# print out all of the sorted items
for k,v in lst:
    print(k,v)
