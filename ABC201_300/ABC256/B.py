
N = int(input())
A = list(map(int, input().split()))

P = 0
stack = []
for a in A:
    if(len(stack) == 0):
        if(3 < a):
            P += 1
        else:
            stack.append(a)
        continue
    tmp = []
    for value in stack:
        v = value + a
        if(3 < v):
            P += 1
        else:
            tmp.append(v)
    if(3 < a):
        P += 1
    else:
        tmp.append(a)
    stack = tmp
print(P)