# 2.3 Write a program to prompt the user for hours and rate per hour using input
# to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the
# program (the pay should be 96.25). You should use input to read a string and
# float() to convert the string to a number. Do not worry about error checking
# or bad user data.

# declare a varibale named "hrs" to let the user input hours by using
# input() function
hrs = input("Enter hours: ")

# declare a vairbale named "rate" to let the user input rate by using
# input() function
rate = input("Enter rates: ")

# print the calculation of hrs * rate
# since "hrs" and "rate" are string data type
# convert them become float as the requirements by using float() function
print("Pay:", float(hrs) * float(rate))
