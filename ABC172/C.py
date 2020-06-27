NMK=input().split(" ")
N=int(NMK[0])
M=int(NMK[1])
K=int(NMK[2])

def list2int(List):
    out=[]
    for i in range(len(List)):
        out.append(int(List[i]))
    return out

A=list2int(input().split(" "))
B=list2int(input().split(" "))

a=[0]
b=[0]
for i in range(N):
    a.append(a[i]+A[i])
for i in range(M):
    b.append(b[i]+B[i])   

result=0
j=M

for i in range(N+1):
    if(a[i]>K):
        break
    while(b[j]>K-a[i]):
        j-=1
    result=max(result,i+j)

print(result)