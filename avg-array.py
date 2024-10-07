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
sum=0
while i<l:
    sum+=L[i]
    i+=1
avg=sum/l
print(avg)