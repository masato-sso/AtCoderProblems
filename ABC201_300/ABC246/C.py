
N, K, X = map(int, input().split())
A = list(map(int, input().split()))


ans = sum(A)

mod = 0
for a in A:
    mod += int(a/X)

mod = min(mod, K)
ans -= mod*X
K -= mod

modA = []
for a in A:
    modA.append(a%X)

sortedA = sorted(modA)[::-1]
for a in sortedA:
    if(K == 0):
        break
    ans -= a
    K -= 1

print(ans)
