word = input()

length = len(word)

i = 0
vCount, cCount = 0, 0

while i < length :
    ch = word[i]
    if (ch >= 'a' and ch <= 'z') or (ch>= 'A' and ch <= 'Z') :

        if (ch == 'a' or ch == 'i' or ch == 'e' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'I' or ch == 'E' or ch == 'O' or ch == 'U') :
            vCount += 1
        else :
            cCount += 1
    i += 1

print (vCount, cCount)
    
