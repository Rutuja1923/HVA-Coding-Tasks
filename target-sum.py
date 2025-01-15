def get_subarray_target_sum(arr, tSum):
    i = 0

    while i < len(arr) :
        j = i
        while j < len(arr):
            k = i
            currSum = 0
            subArr = []
            while k < j+1 :
                currSum += arr[k]
                subArr.append(arr[k])
                k += 1
            if currSum == tSum :
                return subArr
            j += 1
        i += 1

    return []

L=list(map(int, input().split()))
target = int(input())

result = get_subarray_target_sum(L, target)

if result :
    for e in result :
        print(e, end = ' ')
else :
    print("Not Possible")