
N=int(input())

ans=[]

for i in range(1,10):
    for j in range(1,10):
        ans.append(i*j)

if(N in ans):
    print("Yes")
else:
    print("No")
