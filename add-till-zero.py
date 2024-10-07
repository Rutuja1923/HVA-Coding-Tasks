def find_len(lst):
    sum=0
    while lst:
        sum+=1
        lst=lst[1:]
    return sum

print("Enter array elements :")
L=list(map(int,input().split()))

l = find_len(L)
sum = 0
i = 0

while i<l:
    if L[i]==0 : 
        break
    sum+=L[i]
    i+=1
print(sum)
