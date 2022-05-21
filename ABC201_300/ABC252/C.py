
N = int(input())

S = []
for i in range(N):
    S.append(input())

stopMaxTimes = []
for target in range(10):
    tmp = []
    for s in S:
        idx = s.index(str(target))
        while(True):
            if(idx in tmp):
                idx = idx + 10
            else:
                break
        tmp.append(idx)
    stopMaxTimes.append(max(tmp))

ans = min(stopMaxTimes)
print(ans)