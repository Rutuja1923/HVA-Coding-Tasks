def get_max_diff(L):
    minEle=L[0]
    maxEle=L[0]
    i=1 

    while i<len(L):
        if L[i]<minEle:
            minEle = L[i]
        if L[i]>maxEle:
            maxEle = L[i]
        i+=1

    return abs(maxEle-minEle)

def get_min_diff(L):
    i , j = 0,0
    minDiff = float('+inf')
    for i in range(len(L)):
        for j in range(i+1 , len(L)):
            diff = abs(L[i]-L[j])
            if diff < minDiff :
                minDiff = diff
                
    return minDiff

L=list(map(int, input().split()))

print(get_min_diff(L),get_max_diff(L))
