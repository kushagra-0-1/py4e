import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search("^From:", line) : #re.search() returns true/false depending on whether the string matches the regular expression
        print(line)

hand.seek(0,0)

for line in hand:
    line = line.rstrip()
    if re.search("^X.*:", line) : # |^ - startswith| , |. - any character| , |* - 0 or more|
        print(line)

hand.seek(0,0)

for line in hand:
    line = line.rstrip()
    if re.search("^X-\S+:", line) : # |-\S+ - one or more characters without spaces|
        print(line)