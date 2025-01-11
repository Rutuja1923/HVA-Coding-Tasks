def charSearch(word,ch):
    i = 0
    found = False
    while i<len(word):
        if word[i] == ch :
            found = True
            break
        i += 1
    if found :
        return "Yes"
    else:
        return "No"

word = input()
ch = input()
print(charSearch(word,ch))