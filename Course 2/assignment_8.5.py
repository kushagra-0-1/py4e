fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file name. please try again")
lst = list()
count = 0
for line in fh:
    if line.startswith("From"):
        lst = line.split()
        if len(lst) > 2:
            print(lst[1])
            count = count + 1
print("There were", count, "lines in the file with From as the first word")
