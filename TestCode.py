
bool = False
eof = False
check = ""
fileUserID = ""
i = 1
n = 0
searchUserId = ""
searchUserId = input("enter name")
fo = open("test", "r")
line = fo.readline()
while bool == False or len(line) > 0:
    #while check != " ":
    #    check = fo.read(i)
    #    print(check)
    #    i = i + 1
    #    n = n + 1
    #    fo.seek(n)
    #fo.seek(n-i)
    #fileUserID = fo.read(i)
    if fileUserID == searchUserId:
        bool = True
        # read the next line for prefered name until a space is found
        # then assign that name to a variable, then use that to be displayed in a message