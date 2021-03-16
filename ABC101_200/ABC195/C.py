
N=input()
keta=len(N)
N=int(N)

ans=0
for k in range(keta-1,3,-1):
    nine_num=int("9"*k)
    init_num=int("1"+"0"*(k-1))
    num="@".join(list("9"*k))
    comma=int(num.count("@")/3)
    ans+=((nine_num-init_num)+1)*comma

if(keta>3):
    num="@".join(list(str(N)))
    comma=int(num.count("@")/3)
    init_num=int("1"+"0"*(keta-1))
    ans+=((N-init_num)+1)*comma

print(ans)
