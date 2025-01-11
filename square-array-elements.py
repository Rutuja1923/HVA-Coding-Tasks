def squareElem(arr):
    i = 0
    while i < len(arr):
        print(arr[i]**2, end = ' ')
        i += 1

a = list(map(int, input().split()))

squareElem(a)