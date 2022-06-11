
X, A, D, N = map(int, input().split())
def func(n):
    return A + (n - 1) * D

targetN = 1
if(D == 0):
    val = A
else:
    targetN = (X - A + D)//D
    if(targetN > N):
        targetN = N
    if(targetN < 1):
        targetN = 1
    val = func(targetN)

ans = abs(X - val)
if(targetN != N):
    val1 = func(targetN + 1)
    diff = abs(X - val1)
    if(diff < ans):
        ans = diff
if(targetN != 1):
    val2 = func(targetN - 1)
    diff = abs(X - val2)
    if(diff < ans):
        ans = diff

print(ans)