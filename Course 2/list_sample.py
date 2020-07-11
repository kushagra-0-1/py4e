friends = ['Anna', 'Sally', 'Helen']
for friend in friends:
    print(friend)
print(len(friends))

lst = [1, 'hello', 'wow', 3.14]
print(lst[2])
print(len(lst))

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

print(99 in stuff)

friends.sort()
print(friends)

nums = [1, 42, 4, 41, 615]
print(max(nums))
print(min(nums))

abc = "With three spaces"
stuff = abc.split()
print(stuff)

line = 'first;second;third'
thing = line.split(';')
print(thing)

line1 = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line1.split()
pieces = words[1].split('@')
print(pieces[1])
