def palin(x):
    y=1
    if len(x)<2:
        return(True)
    else:
        for a in range (0,int(len(x)/2)):
            if x[a]!=x[len(x)-y]:
                return(False)
            if x[a]==x[len(x)-y]:
                y=y+1
        return(True)
f,g=0,0
for a in reversed(range(1,1000)):
    for b in reversed(range(1,1000)):
            if palin(str(a*b)):
                    g=a*b
                    if g>f:
                        f,g=g,0
print(f)
