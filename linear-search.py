def find_len(lst):
    sum=0
    while lst:
        sum+=1
        lst=lst[1:]
    return sum

print("Enter array elements :")
L=list(map(int,input().split()))
key = int(input("Enter the key to be searched : "))

l = find_len(L)
found = False
i = 0

while i<l :
    if L[i]==key:
        found = True
        break
    i+=1
if found:
    print("Yes")
else :
    print("No")
    

