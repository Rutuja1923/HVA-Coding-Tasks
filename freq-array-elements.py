def get_freq_each_element(L):
    freq = {}

    i = 0
    while i < len(L) :
        currELe = L[i]
        if currELe in freq :
            freq[currELe] += 1
        else:
            freq[currELe] = 1
        i += 1

    j = 0
    elements = list(freq.keys())
    while j < len(elements) :
        print(elements[j], freq[elements[j]])
        j += 1

L=list(map(int, input().split()))

get_freq_each_element(L)

