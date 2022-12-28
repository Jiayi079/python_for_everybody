# 3.1 Write a program to prompt the user for hours and rate per hour using input
# to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times
# the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate
# of 10.50 per hour to test the program (the pay should be 498.75). You should
# use input to read a string and float() to convert the string to a number. Do
# not worry about error checking the user input - assume the user types numbers
# properly.

# initial hrs to let the user input hours -> type() is str
hrs = input("Enter Hours:")
# convert hrs to float data type and put it into vairable named "h"
h = float(hrs)

# initial rate to let the user input rate -> type() is str
rate = input("Enter Rates: ")
# convert rate to float data type and put it into vairable named "r"
r = float(rate)

# starting condiction
# check if h is larger than 40
if h > 40 :
    # line 24 will run if only if h is larger than 40
    # calculate the pay result by using calculation
    pay = 40 * r + (h - 40) * r * 1.5
else :
    # line 28 will run if only if "h > 40" condiction is false
    # do calculation to get the pay result
    pay = h * r

# print() function used to print the pay result
print(pay)
