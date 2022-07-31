
N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    A[i] -= 1

n = 0
for i,x in enumerate(A):
    if(i == x):
        n += 1

ans = n*(n - 1) // 2
for i,j in enumerate(A):
    if(i < j and A[j] == i):
        ans += 1

print(ans)