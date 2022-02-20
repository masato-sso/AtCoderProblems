
N, X = map(int, input().split())
dp = 1
for i in range(N):
    a,b = map(int, input().split())
    dp = (dp << a) | (dp << b)

if((dp >> X) & 1):
    print("Yes")
else:
    print("No")
