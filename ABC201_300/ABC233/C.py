import itertools

N, X = map(int, input().split())
L = []
for i in range(N):
    L.append(list(map(int, input().split()))[1:])

cans = list(itertools.product(*L))
ans = 0
for can in cans:
    calc = 1
    for num in can:
        calc *= num
    if (calc == X):
        ans +=1

print(ans) 
