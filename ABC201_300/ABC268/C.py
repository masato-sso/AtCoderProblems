
N = int(input())
p = list(map(int, input().split()))

cnt = [0] * N
for i in range(N):
    for j in range(3):
        cnt[(p[i]-1-i+j+N)%N]+=1

ans = 0
for i in range(N):
    ans = max(ans, cnt[i])

print(ans)