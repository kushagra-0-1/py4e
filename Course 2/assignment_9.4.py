name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
words = list()
for line in handle:
    if line.startswith('From'):
        words = line.split()
        if len(words) > 2:
            counts[words[1]] = counts.get(words[1], 0) + 1

max_sender = None
max_send = None
for k,v in counts.items():
    if max_send is None or v > max_send:
        max_sender = k
        max_send = v

print(max_sender, max_send)