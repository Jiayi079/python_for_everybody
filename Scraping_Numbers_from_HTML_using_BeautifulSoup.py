# Scraping Numbers from HTML using BeautifulSoup In this assignment you will
# write a Python program similar to http://www.py4e.com/code3/urllink2.py. The
# program will use urllib to read the HTML from the data files below, and parse
# the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give
# you the sum for your testing and the other is the actual data you need to
# process for the assignment.
# 1. Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# 2. Actual data: http://py4e-data.dr-chuck.net/comments_1710366.html (Sum ends with 15)

# You do not need to save these files to your folder since your program will
# read the data directly from the URL. Note: Each student will have a distinct
# data url for the assignment - so only use your own data url for analysis.

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# import urllib and BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# let the user input url
url = input('Enter - ')
# open url to read
html = urlopen(url, context=ctx).read()
# get the html data from website by ysing BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# initialize two varibales to calculate the sum and the count
sum = 0
count = 0

# Retrieve all of the anchor tags
# find all the <span> tag in the file
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)

    # pull out the number from the tag and sum the numbers
    sum = sum + int(tag.contents[0])
    count = count + 1

print("Count", count)
print("Sum", sum)
