def wordSearch(sentence, key):
    m = len(sentence)
    n = len(key)

    found = False

    i = 0
    while i < m - n + 1:
        j = 0
        while j < n :
            if sentence[i+j] != key[j] :
                break
            j += 1

        if j == n :
            found = True
            break
        i += 1

    if found :
        return "Yes"
    else :
        return "No"
    

sentence = input()
word = input()

print(wordSearch(sentence, word))
