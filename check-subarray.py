def check_subarrray(arr, targetSubArr):
    i = 0

    if len(arr) < len(targetSubArr) :
        return "No"
    
    while i < len(arr) :
        j = i
        subArr = []
        while j < len(arr):
            subArr.append(arr[j])
            if len(subArr) == len(targetSubArr) and subArr == targetSubArr:
                return "Yes"
            j += 1
        i += 1

    return "No"

L = list(map(int, input().split()))
target = list(map(int, input().split()))

print(check_subarrray(L,target))

