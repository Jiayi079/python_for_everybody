# 5.2 Write a program that repeatedly prompts a user for integer numbers until
# the user enters 'done'. Once 'done' is entered, print out the largest and
# smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the
# number. Enter 7, 2, bob, 10, and 4 and match the output below.

# initial "largest" and "smallest" variable become "None" firstly
# largest -> to keep the largest number
# smallest -> to keep the smallest number
largest = None
smallest = None

# indefinite loops
# while True will make this loop becomes infinite loop
while True:
    # let the user input a str
    num = input("Enter a number: ")

    # check if the user input "done", which means user want to exit
    if num == "done":
        break   # break outside of the loop

    # catch error if user input invalid input
    try:
        n = int(num)    # convert num to integer
    except:
        print("Invalid input")
        continue    # continue to the top of the loop to start a new iteration
                    # it will happens if only if the user input is invalid

    # check if the "largest" and "smallest" variables are "None"
    # which means we just start the while loop and nothing inside of those two
    # vairables, then, we need put the first number into those two variables
    # those two if-statement will only execute at the frist time of the loop
    if largest is None:
        largest = n
    if smallest is None:
        smallest = n

    # check if the number "n" is largger than the number "largest" keeps before
    if largest < n:
        largest = n     # if true, we update the largest number

    # check if the number "n" is smaller than the number "smallest" keeps before
    if smallest > n:
        smallest = n    # if true, we update the smallest number

# print out the result
print("Maximum is", largest)
print("Minimum is", smallest)
