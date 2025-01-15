def isValidPassword(pwd) :
    i = 0
    l = len(pwd)

    if l < 8 : 
        return False
    
    hasLower = False
    hasUpper = False
    hasDigit = False
    hasSpecial = False
    specialChars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    while i < l :
        ch = pwd[i]
        if ch.islower() :
            hasLower = True
        elif ch.isupper() :
            hasUpper = True
        elif ch.isdigit():
            hasDigit = True
        elif ch in specialChars :
            hasSpecial = True
        i += 1
    
    return hasLower and hasUpper and hasDigit and hasSpecial

password = input()
if isValidPassword(password) :
    print("Yes")
else :
    print("No")

