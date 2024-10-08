def find_len(lst):
    sum=0
    while lst:
        sum+=1
        lst=lst[1:]
    return sum

print("Enter array elements :")
L=list(map(int,input().split()))

l = find_len(L)
i = 0
j = l-1

while i<j :
    L[i] , L[j] = L[j] , L[i]
    i+=1
    j-=1

for k in L:
    print(k,end=' ')
    

