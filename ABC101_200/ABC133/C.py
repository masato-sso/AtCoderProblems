
S=input()

tmp=S.split()

L=int(tmp[0])
R=int(tmp[1])

R=min(L+2019,R)

flag=False
result=1000000000000
for i in range(L,R+1):
    for j in range(i+1,R+1):
        if i>=j:
            flag=True
            break
        n=(i*j)%2019
        if result>n:
            result=n
    if(flag):
        break



print(result)
