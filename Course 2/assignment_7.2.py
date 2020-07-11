try :
    fname = input("Enter file name: ")
except :
    print("No such file exists!")
    quit()

count = 0
avg = 0.0
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        num_pos = line.find( '0' )
        num = float(line[num_pos:])
        avg = avg + num
avg = avg / float(count)
avg = str(avg)
print("Average spam confidence: " + avg)
