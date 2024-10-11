def find_len(lst):
    count=0
    while lst:
        count+=1
        lst=lst[1:]
    return count

def get_min_max(L, length):
    minEle=L[0]
    maxEle=L[0]
    i=1 

    while i<length:
        if L[i]<minEle:
            minEle = L[i]
        if L[i]>maxEle:
            maxEle = L[i]
        i+=1

    return (minEle,maxEle)

def get_min_diff(L,length):
    i , j = 0,0
    minDiff = float('+inf')
    for i in range(length):
        for j in range(length):
            if L[i]-L[j] < minDiff :
                minDiff = L[i]-L[j]
    return minDiff


print("Enter array elements :")
L=list(map(int,input().split()))
l = find_len(L)

minEle,maxEle = get_min_max(L ,l)

maxDiff = maxEle-minEle
minDiff = get_min_diff(L,l)
print(maxDiff , minDiff)
