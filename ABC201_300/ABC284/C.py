from collections import defaultdict, deque

N, M = map(int, input().split())
visited = [False]*(N+1)
UV = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    UV[u].append(v)
    UV[v].append(u)

ans = 0
for i in range(1,N+1):
    if(visited[i]):
        continue
    que = deque()
    que.append(i)
    visited[i] = 0
    while que:
        now = que.popleft()
        for to in UV[now]:
            if(not(visited[to])):
                visited[to] = True
                que.append(to)
    ans += 1

print(ans)