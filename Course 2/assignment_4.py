def computepay(h, r):
    pay = 0
    if h>40 :
        pay = 40*r + (h-40)*r*1.5
    else :
        pay = h*r;
    return pay
hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
print("Pay", computepay(hrs, rate))
