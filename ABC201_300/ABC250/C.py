
N, Q = map(int, input().split())

X = []
for i in range(Q):
    X.append(int(input()))

balls = list(range(0, N + 1))
pos = list(range(0, N + 1))


for i in range(Q):
    ballIdx = pos[X[i]]
    if(ballIdx == N):
        tmp = pos[X[i]]
        pos[X[i]] = pos[balls[ballIdx - 1]]
        pos[balls[ballIdx - 1]] = tmp

        tmp = balls[ballIdx]
        balls[ballIdx] = balls[ballIdx - 1]
        balls[ballIdx - 1] = tmp
    else:
        tmp = pos[X[i]]
        pos[X[i]] = pos[balls[ballIdx + 1]]
        pos[balls[ballIdx + 1]] = tmp

        tmp = balls[ballIdx]
        balls[ballIdx] = balls[ballIdx + 1]
        balls[ballIdx + 1] = tmp

balls.remove(0)
ans = " ".join(list(map(str, balls)))
print(ans)
