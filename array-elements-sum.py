def getSumArray(arr):
    i = 0
    
    sumArr = []

    while i < len(arr):
        j = 0
        currSum = 0
        while j < len(arr) :
            if i != j :
                currSum += arr[j]
            j += 1
        sumArr.append(currSum)
        i += 1
    k = 0
    while k < len(sumArr) :
        print(sumArr[k], end = ' ')
        k += 1


L=list(map(int, input().split()))
getSumArray(L)