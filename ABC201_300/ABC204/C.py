import sys
sys.setrecursionlimit(10000)

N,M=map(int,input().split())

G=[[] for i in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    G[a-1].append(b-1)

def dfs(v):
    if temp[v]: return
    temp[v]=True
    for vv in G[v]:
        dfs(vv)

ans=0

for i in range(N):
    temp=[False]*N
    dfs(i)
    ans+=sum(temp)

print(ans)
