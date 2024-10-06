N = int(input("Enter a number : "))
i = 1
while i<=N:
    k = N - i
    while(k>0):
        print(" ",end="")
        k-=1 
    j = 1
    while j<=i : 
        print("*",end="")
        j+=1
    print()
    i+=1