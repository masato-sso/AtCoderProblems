from collections import defaultdict

N = int(input())
ST = defaultdict(lambda: 0)
Submit = {}
S = []
for i in range(N):
    s, t = map(str, input().split())
    if(ST[s] != 0):
        continue
    ST[s] = int(t)
    Submit[s] = (i + 1)
    S.append(s)

max_score = -1
ans = -1
for idx,s in enumerate(S):
    val = ST[s]
    if(max_score < val):
        max_score = val
        ans = Submit[s]

print(ans)