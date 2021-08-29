N=int(input())

S=[]
T=[]
for i in range(N):
    s,t=map(str,input().split())
    S.append(s)
    T.append(t)

find=False
for i in range(N):
    s1=S[i]
    t1=T[i]
    for j in range(i+1,N):
        s2=S[j]
        t2=T[j]
        if(s1==s2 and t1==t2):
            find=True
            break

if(find):
    print("Yes")
else:
    print("No")
