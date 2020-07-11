m = input()
n = int(m)
if n % 2 == 1:
    print("Weird")
else:
    if n >= 2 and n <= 5:
        print("Not Weird")
    if n > 5 and n <= 20:
        print("Weird")
    if n > 20:
        print("Not Weird")