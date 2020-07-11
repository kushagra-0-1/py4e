import re
sum = 0
data = open("regex_sum_437285.txt")
for line in data:
    line = line.rstrip()
    numlist = re.findall("[0-9]+", line)
    for num in numlist:
        sum = sum + int(num)
    numlist.clear()
print(sum)