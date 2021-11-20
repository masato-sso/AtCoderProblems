
N,X = map(int, input().split())
A = list(map(int, input().split()))
 
knew = set([X])
next = A[X - 1]
ans = 1
for i in range(N):
    if(next in knew):
        break
    knew.add(next)
    next = A[next - 1]
    ans += 1

print(ans)