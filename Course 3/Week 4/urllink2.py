# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
sum = 0
i = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    a = tag.contents
    num = (int)(a[0-1])
    if isinstance(num, int):
        sum += num
        i += 1
print("Count ", i)
print("Sum ", sum)