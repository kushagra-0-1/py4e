fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtp = (val, key)
    lst.append(newtp)

lst = sorted(lst, reverse = True)

for val,key in lst[:10]:
    print(key, val)


#the above 3 segments can be written in a single line as:
#print(sorted([(v,k) for (k,v) in counts.items()], reverse = True))
