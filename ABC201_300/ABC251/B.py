import itertools

N, W = map(int, input().split())
A = list(map(int, input().split()))

cans = []
combA = itertools.combinations(A, 1)
for com in combA:
    cans.append(sum(com))
combA = itertools.combinations(A, 2)
for com in combA:
    cans.append(sum(com))
combA = itertools.combinations(A, 3)
for com in combA:
    cans.append(sum(com))

cans = list(set(cans))
check = []
for can in cans:
    if(can <= W):
        check.append(can)

ans = len(check)

print(ans)