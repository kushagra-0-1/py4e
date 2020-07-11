import re
x = "My 2 favourite numbers are 19 and 42"
y = re.findall('[0-9]+', x)
print(y)

y = re.findall('[AEIOU]+', x)
print(y)

# Both * and + are greedy, i.e., they want to extend as large as possible
# Therefore, we use ? after + for non-greedy like: +?

x = open('mbox-short.txt')

for line in x:
    line = line.rstrip()
    y = re.findall('^From (\S+@\S+)', line)
    print(y)

x.seek(0,0)
for line in x:
    line = line.rstrip()
    y = re.findall('^From .*@([^ ]*)', line)
    print(y)

x.seek(0,0)
numlist = list()
for line in x:
    line = line.rstrip()
    y = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(y) != 1: continue
    num = float(y[0])
    numlist.append(num)
print("Maximum:", max(numlist))