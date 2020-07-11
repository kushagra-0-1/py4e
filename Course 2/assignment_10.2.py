name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
words = list()
hrs = list()
for line in handle:
    if line.startswith('From'):
        words = line.split()
        if len(words) > 2:
            word = words[5]
            hrs = word.split(':')
            counts[hrs[0]] = counts.get(hrs[0], 0) + 1

lst = list()
for key, val in counts.items():
    newtp = (key, val)
    lst.append(newtp)

lst = sorted(lst)

for key,val in lst:
    print(key, val)