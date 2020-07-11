ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#for name in names:
#    if name not in counts:
#        counts[name] = 1
#    else:
#        counts[name] += 1
#print(counts)

x = counts.get('bob', 0)
print(x)

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

print(counts.keys())
print(counts.values())
print(counts.items())

for aaa,bbb in counts.items():
    print(aaa,bbb)