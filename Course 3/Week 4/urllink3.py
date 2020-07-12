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

url = input('Enter URl: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Input info from user
count = int(input("Enter Count: "))
position = int(input("Enter position: "))
c = 0
p = 0

# Retrieve all of the anchor tags
tags = soup('a')
print("Retrieving: ", url)

while c < count:
    while p < position - 1:
        tags[p].get('href', None)    
        p += 1
    print('Retrieving: ', tags[p].get('href', None))
    url = tags[p].get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    p = 0
    c += 1