n = int(input("Enter a number : "))
c = 0
i = 2
flag = False
while(c < n):
    flag = True
    f = int(i ** 0.5) + 1
    j=2
    while j<f:
        if (i%j == 0):
            flag = False
            break
        j += 1
    if(flag):
        print(i, end=" ")
        c+=1
    i+=1