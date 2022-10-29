
N = int(input())
H = list(map(int, input().split()))

maxValue = max(H)

ans = 0
for idx,h in enumerate(H):
    if(h == maxValue):
        ans = idx + 1
        break

print(ans)