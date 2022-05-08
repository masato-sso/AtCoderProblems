
H, W = map(int, input().split())
R, C = map(int, input().split())

ans = 0

if(0 < (R - 1)):
    ans += 1
if((R + 1) < (H + 1)):
    ans += 1
if(0 < (C - 1)):
    ans += 1
if((C + 1) < (W + 1)):
    ans += 1

print(ans)