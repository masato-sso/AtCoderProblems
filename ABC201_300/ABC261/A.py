
L1, R1, L2, R2 = map(int, input().split())

red = list(range(L1, R1 + 1))
blue = list(range(L2, R2 + 1))

ans = []
for r in red:
    if(r in blue):
        ans.append(r)

if(0 < len(ans)):
    print(max(ans)-min(ans))
else:
    print(0)