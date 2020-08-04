a=0
for i in range (0,1000):
    if(i%3==0):
        a=a+i
    elif (i%5==0):
        a=a+i
    else:
        a=a+0
print(a)