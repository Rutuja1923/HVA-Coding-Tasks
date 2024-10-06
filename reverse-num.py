N=int(input("Enter a number : "))
revNum=0
num=N
while (num>0):
    r = num%10
    revNum=revNum*10+r
    num//=10
print(revNum)