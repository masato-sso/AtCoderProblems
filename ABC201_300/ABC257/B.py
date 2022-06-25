
N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

tmpA = A
for idx in L:
    idx = idx - 1
    koma = tmpA.pop(idx)
    target = koma + 1
    if(N < target):
        tmpA.insert(idx, koma)
        continue 
    if(target in tmpA):
        tmpA.insert(idx, koma)
        continue
    tmpA.insert(idx, target)

ans = ""
for i in range(len(tmpA)):
    t = tmpA[i]
    ans = ans + str(t)
    if(i == len(tmpA) - 1):
        break
    ans = ans + " "

print(ans)
