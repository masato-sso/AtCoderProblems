
N = int(input())

S = []
T = []

for i in range(N):
    s, t = map(str, input().split())
    S.append(s)
    T.append(t)

yesFlag = True
for i in range(N):
    s1 = S[i]
    t1 = T[i]
    # s check
    checkFlag1 = True
    for j in range(N):
        if(i == j):
            continue
        s2 = S[j]
        t2 = T[j]
        if(s1 == s2 or s1 == t2):
            checkFlag1 = False
    if(checkFlag1):
        continue
    # t check
    checkFlag2 = True
    for j in range(N):
        if(i == j):
            continue
        s2 = S[j]
        t2 = T[j]
        if(t1 == s2 or t1 == t2):
            checkFlag2 = False
    if(checkFlag2):
        continue
    yesFlag = False
    break

if(yesFlag):
    print("Yes")
else:
    print("No")
