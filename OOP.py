def valid(s):
    global isValid
    digits = ['0','1','2','3','4','5','6','7','8','9']
    isValid = False
    if len(s) == 4:
        if (s[0] in digits) & (s[1] in digits) & (s[2] in digits) & (s[3] in digits):
            isValid = True
    return isValid

print(valid("1234"))