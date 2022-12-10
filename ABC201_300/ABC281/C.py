
N, T = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)

remain = T % total

for i in range(N):
    diff = remain - A[i]
    if(diff < 0):
        print(i+1, remain)
        exit(0)
    remain = remain - A[i]

