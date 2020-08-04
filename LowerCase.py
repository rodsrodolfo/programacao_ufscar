def lowerChar(char):
    output=""
    for x in range(0,len(char)):
        if ord(char[x])<=90 and ord(char[x])>=65:
            output=output+chr(ord(char[x])+32)
        else:
            output=output+char[x]
    return(output)
while(0==0):
    char=input()
    print(lowerChar(char))
    print('**********')