def getFirstRepeat(arr):
    i = 0
    temp = []

    while i < len(arr):
        if arr[i] in temp :
            return arr[i]
        temp.append(arr[i])
        i += 1
    return "No"
L = list(map(int, input().split()))
print(getFirstRepeat(L))
