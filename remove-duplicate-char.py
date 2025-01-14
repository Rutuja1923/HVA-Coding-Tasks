def removeDuplicate(word):
    i = 0
    newWord = ''
    while i<len(word):
        if word[i] not in newWord :
            newWord = newWord + word[i]
        i += 1
    return newWord

word = input()
print(removeDuplicate(word))
