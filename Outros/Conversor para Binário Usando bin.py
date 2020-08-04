print('**********')
while(0==0):
    x=bin(int(input('Your number:')))
    y=''
    for i in range (2,len(str(x))):
        y=y+x[i]
    print('In binary:',y)
    print('**********')