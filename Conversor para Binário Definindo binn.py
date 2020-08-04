print('**********')
while(0==0):
    def binn(x):
        list=[]
        w=""
        while(x>0):
            a,b=divmod(x,2)
            x=a
            list.append(1)
            list[len(list)-1]=b
        while(len(list)>0):
            w=w+str(list[len(list)-1])
            del(list[len(list)-1])
        print('In binary:',w)
        print('**********')
    binn(int(input('Your number:')))