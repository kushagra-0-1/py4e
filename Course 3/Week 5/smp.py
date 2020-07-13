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
data.decode()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print("Count: ", len(counts))
sum = 0
for num in counts:
    sum = sum + int(num)
print("Sum: ", sum)