from collections import defaultdict

S = input()

d = defaultdict(int)

size = len(S)
skip = False
for i in range(size):
    if(skip):
        skip = False
        continue
    s = S[i]
    if((s == "0") and ((i+1) < size) and (S[i+1] == "0")):
        d["00"] += 1
        skip = True
        continue
    d[s] += 1

ans = 0
for key in d:
    ans += d[key]
        
print(ans)