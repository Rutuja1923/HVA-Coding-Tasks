def areAnagram(word1,word2):
    s1 = ''
    s2 = ''
    i, j = 0, 0
    while i< len(word1):
        if word1[i] != ' ':
            s1 += word1[i].lower()
        i += 1
    while j< len(word2):
        if word2[j] != ' ':
            s2 += word2[j].lower()
        j += 1

    if len(s1) != len(s2):
        return "No"
    
    dict1 = {}
    i = 0 
    while i < len(s1):
        ch = s1[i]
        if ch in dict1:
            dict1[ch] += 1
        else :
            dict1[ch] = 1
        i += 1

    dict2 = {}
    j = 0 
    while j < len(s2):
        ch = s2[j]
        if ch in dict2:
            dict2[ch] += 1
        else :
            dict2[ch] = 1
        j += 1  

    if dict1 == dict2 :
        return "Yes"
    else:
        return "No"


w1 = input()
w2 = input()

print(areAnagram(w1,w2))