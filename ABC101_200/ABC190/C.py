import itertools

N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]
K = int(input())
CD = [tuple(map(int, input().split())) for i in range(K)]

ans = 0
for balls in itertools.product(*CD):
    balls = set(balls)
    cnt = sum(a in balls and b in balls for a, b in AB)
    if ans < cnt:
        ans = cnt
print(ans)