from collections import deque

N, X, Y = map(int, input().split())
UV = [[] for i in range(N+1)]

for i in range(N-1):
    u,v = map(int,input().split())
    UV[u].append(v)
    UV[v].append(u)
 
depth = [-1] * (N+1)
rec = [[] for i in range(N+1)]

def dfs(v,u):    
    dq = deque()
    dq.append([v,0])
    while dq:
        x,d = dq.popleft()
        depth[x] = d
        rec[d].append(x)
        if x == u:
            break
        for y in UV[x]:
            if depth[y] >= 0:
                continue
            dq.append([y,d+1])
 
dfs(Y,X)
ans = [str(X)]
length = depth[X]
 
p = X
for u in range(length,-1,-1):
    for v in rec[u]:
        if v in UV[p]:
            ans.append(str(v))
            p = v

result = " ".join(ans)
print(result)