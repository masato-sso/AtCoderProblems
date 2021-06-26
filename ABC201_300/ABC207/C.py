
N=int(input())

toler=0.000001
tlr_l=[]
tlr_r=[]
for i in range(N):
    t,l,r=map(int,input().split())
    if(t==1):
        tlr_l.append(l)
        tlr_r.append(r)
    elif(t==2):
        tlr_l.append(l)
        tlr_r.append(r-toler)
    elif(t==3):
        tlr_l.append(l+toler)
        tlr_r.append(r)
    else:
        tlr_l.append(l+toler)
        tlr_r.append(r-toler)

ans=0
for i in range(N):
    for j in range(i+1,N):
        target_l=max(tlr_l[i],tlr_l[j])
        target_r=min(tlr_r[i],tlr_r[j])
        diff=target_r-target_l
        if(diff>=0):
            ans+=1

print(ans)