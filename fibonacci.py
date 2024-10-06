N=int(input("Enter a number : "))
f1=0
f2=1
if(N==0):
    print("Kindly enter a number greater than 0")
elif(N==1):
    print(f1)
elif(N==2):
    print(f1,f2)
else:
    c=3
    print(f1,f2,end=' ')
    while (c<=N):
        fib=f1+f2
        f1=f2
        f2=fib
        c+=1
        print(fib,end=' ')