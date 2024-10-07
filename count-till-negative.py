def find_len(lst):
    count=0
    while lst:
        count+=1
        lst=lst[1:]
    return count

print("Enter array elements :")
L=list(map(int,input().split()))

l = find_len(L)
count = 0
i = 0

while i<l:
    if L[i]<0 : 
        break
    i+=1
    count+=1
print(count)
