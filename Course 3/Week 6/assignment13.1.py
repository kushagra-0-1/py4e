import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    data = json.loads(html)
    print('Retrieveig', len(data), 'characters')
    sum = 0
    count = 0

    for item in data["comments"]:
        sum = sum + item["count"]
        count = count + 1

    print("Count: ", count)
    print("Sum: ", sum)