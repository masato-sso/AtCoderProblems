
N = int(input())
A = list(map(int, input().split()))

maxA = max(A)
sortedA = sorted(list(set(A)))

cans = list(range(0, maxA + 1))

ans = -1
for can in cans:
    if(can in sortedA):
        continue
    ans = can
    break

if(ans == -1):
    ans = maxA + 1

print(ans)
