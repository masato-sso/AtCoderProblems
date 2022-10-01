
N = int(input())
A = list(map(int, input().split()))
setA = set(A)

cur = 0
for i in range(1, N + 1):
    cur += (i in setA)
    if((N - cur) < (i - cur)*2):
        print(i - 1)
        exit(0)

print(N)