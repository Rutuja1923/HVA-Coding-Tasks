dec = int(input("Enter a decimal number : "))
bin , d = 0 , 1
while dec>0:
    r = dec%2
    dec = dec//2
    bin = bin+r*d
    d*=10
print(bin)