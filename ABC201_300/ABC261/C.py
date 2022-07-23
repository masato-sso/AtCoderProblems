from collections import defaultdict

N = int(input())

S = []
for i in range(N):
    S.append(input())

cntDict = defaultdict(int)

for s in S:
    if(cntDict[s] == 0):
        print(s)
    else:
        print(s + "(" + str(cntDict[s]) + ")")
    cntDict[s] += 1
