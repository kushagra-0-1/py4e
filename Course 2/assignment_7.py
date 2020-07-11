try :
    fname = input("Enter file name:")
except :
    print("The file does not exist")
    quit()

fh = open(fname)
for line in fh :
    x = line.rstrip()
    print(x.upper())
