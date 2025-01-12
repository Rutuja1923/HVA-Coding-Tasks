def get_sub_array_sum(L):
    l = len(L)
    totalSum = 0

    i = 0
    while i < l :
        currSum = 0
        j = i
        while j < l :
            currSum += L[j]
            totalSum += currSum
            j += 1
        i += 1
    
    return totalSum

L=list(map(int, input().split()))

print(get_sub_array_sum(L))

