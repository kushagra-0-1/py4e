fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File not found, Please try again")
lst = list()
lst1 = list()
for line in fh:
    line = line.strip()
    lst = line.split()
    for word in lst:
        if not word in lst1:
            lst1.append(word)
lst1.sort()
print(lst1)