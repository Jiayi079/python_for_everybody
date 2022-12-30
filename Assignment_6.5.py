# 6.5 Write code using find() and string slicing (see section 6.10) to extract
# the number at the end of the line below. Convert the extracted value to a
# floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

# set up an index integer to keep the finding index
index = -1

# use find() function to find the ":" character in the text string
index = text.find(':')

# check if we find ":"
if index != -1:
    # get the last part of the string whcih is before ":"
    str = text[index+1:]
else:
    # print message will print out if only if we didn't find ":"
    print("can't find number in text")

# removes whitespace at the left by using lstrip() functrion
# convert this string become float by using float() function
print(float(str.lstrip())
