bin = int(input("Enter a binary number : "))
n = bin
dec,base = 0,1
while n>0 :
    r = n%10
    n = n//10
    dec = dec + r * base
    base*=2  
print(int(dec))