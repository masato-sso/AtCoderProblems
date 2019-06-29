S=input()

if (len(S)==4):
    w=[]
    for x in S:
        w.append(x)
    c=dict(zip(w,[0]*len(w)))
    b=[0]*len(c)
    a=dict(zip(w,b))
    if (len(c)==2):
        flag=True
        for t in w:
            c[t]=c[t]+1
        for t in w:
            if c[t]!=2:
                flag=False
        if(flag):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

