# 4.6 Write a program to prompt the user for hours and rate per hour using input
# to compute gross pay. Pay should be the normal rate for hours up to 40 and
# time-and-a-half for the hourly rate for all hours worked above 40 hours. Put
# the logic to do the computation of pay in a function called computepay() and
# use the function to do the computation. The function should return a value.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should
# be 498.75). You should use input to read a string and float() to convert the
# string to a number. Do not worry about error checking the user input unless
# you want to - you can assume the user types numbers properly. Do not name your
# variable sum or use the sum() function.

def computepay(h, r):
    # convert hrs to float data type and put it into vairable named "h"
    h = float(hrs)
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
    return pay

# initial hrs to let the user input hours -> type() is str
hrs = input("Enter Hours: ")
# initial rate to let the user input rate -> type() is str
rate = input("Enter Rates: ")
# call computepay() function with two arguments: "hrs" and "rate"
p = computepay(hrs, rate)

# print() function used to print the pay result
print("Pay", p)
