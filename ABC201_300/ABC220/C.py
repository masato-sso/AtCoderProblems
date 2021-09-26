
N=int(input())
A=list(map(int,input().split()))
X=int(input())
accum_A=[0]
for idx in range(N):
    accum_A.append(accum_A[idx]+A[idx])

size_A=N
sum_A=sum(A)
div=X//sum_A
mod=X%sum_A

ans=size_A*div

for i in range(N+1):
    if(mod<accum_A[i]):
        ans=ans+i
        break

print(ans)