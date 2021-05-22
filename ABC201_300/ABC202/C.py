import collections

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

B_from_C=[]
for i in range(N):
    B_from_C.append(B[C[i]-1])

counter_A=collections.Counter(A)
counter_B=collections.Counter(B_from_C)

ans=0
keys=list(counter_A.keys())
for key in keys:
    ans+=counter_A[key]*counter_B[key]

print(ans)