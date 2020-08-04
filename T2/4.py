l=[]
for a in reversed(range(1000)):
    for b in reversed(range(1000)):
        if str(a*b)==str(a*b)[::-1]:
            l.append(a*b)
print(max(l))
