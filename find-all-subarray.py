def get_all_subarrays(arr):
    i = 0
    while i < len(arr) :
        j = i
        while j < len(arr):
            k = i
            while k < j+1 :
                print(arr[k], end= ' ')
                k += 1
            print()
            j += 1
        i += 1
    return

L=list(map(int, input().split()))
get_all_subarrays(L)

