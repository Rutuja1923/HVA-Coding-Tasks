def capitalize_n_th_character(w,n):
    i = 0
    new_word = ''
    while i < len(w) :
        if i == n :
            new_word += w[i].upper()
        else :
            new_word += w[i]
        i += 1
    
    return new_word

word = input()
n = int(input())

print(capitalize_n_th_character(word,n))

