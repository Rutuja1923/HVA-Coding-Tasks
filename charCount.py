def charCount(word,ch):
    i = 0
    freq = 0
    while i<len(word):
        if word[i] == ch :
            freq += 1
        i += 1
    return freq

word = input()
ch = input()
result = charCount(word,ch)
if (result):
    print(result)
else:
    print("No")