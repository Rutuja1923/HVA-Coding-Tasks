n = int(input("Enter a number : "))
flag , i = 0 , 2
while i<n:
    if n%i == 0:
        flag=1
        break
    i+=1
if flag:
    print("No")
else:
    print("Yes")