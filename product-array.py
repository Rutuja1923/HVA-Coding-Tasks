def find_len(lst):
    count=0
    while lst:
        count+=1
        lst=lst[1:]
    return count
print("Enter array elements :")
L=list(map(int,input().split()))
l = find_len(L)
i=0
prod=1
while i<l:
    prod*=L[i]
    i+=1
print(prod)