N=int(input("Enter a number : "))
c=1
while (c<=N):
    if(N%c==0):
        print(c,end=" ")
    c+=1
