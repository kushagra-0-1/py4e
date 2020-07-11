try :
    fname = input("Enter file name:")
except :
    print("The file does not exist")
    quit()

count = 0
fh = open(fname)
for line in fh :
    count = count + 1
    x = line.rstrip()
    print(x.upper())
print(count)