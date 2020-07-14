import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
html = urllib.request.urlopen(url, context=ctx)

print('Retrieving', url)
data = html.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
count = 0
sum = 0
for item in counts:
    x = int(item.find('count').text)
    count += 1
    sum += x
print("Count: ", count)
print("Sum: ", sum)