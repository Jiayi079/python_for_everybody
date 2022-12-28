# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is
# out of range, print an error. If the score is between 0.0 and 1.0, print a
# grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and
# exit. For the test, enter a score of 0.85.

# declare score variable to let the user input the value of score
score = input("Enter your score: ")

# do try-except stucture
# catch the error if user input an invalid variable
try :
    s = float(score)
except :
    # if score is invalid to convert to float data type
    # set s = -1 to make sure the program is on the right track
    s = -1

# check if s is equal to -1, whcih means failed to convert user input to become
# a float variable
if s == -1 : 
    grade = "Error for convert your input to float data type"
elif s >= 0.9 :  # check other process by ysing elif statement
    grade = "A"
elif s >= 0.8 :
    grade = "B"
elif s >= 0.7 :
    grade = "C"
elif s >= 0.6 :
    grade = "D"
elif s < 0.6 :
    grade = "F"

# print out grade
# will printout "Error..." if invalid convert score as what mentioned before on
# line 25
print(grade)
