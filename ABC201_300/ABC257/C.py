
N = int(input())
S = list(map(int, input()))
W = list(map(int, input().split()))

sortedW = sorted(zip(W,S))

cnt = sum(S)
base = 0
ans = cnt
for w,s in sortedW:
    if (base != w):
        ans = max(ans, cnt)
        base = w
    if(s == 0):
        cnt += 1
    else:
        cnt -= 1
    
ans = max(ans, cnt)
print(ans)