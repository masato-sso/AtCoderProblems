import itertools
import collections

N, K = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

result = []
for n in range(1, len(S) + 1):
    for conb in itertools.combinations(S, n):
        result.append(list(conb))

cnt = [0] * len(result)

for i in range(len(result)):
    elemList = itertools.chain.from_iterable(result[i])
    c = collections.Counter(elemList)
    counter = list(c.values())
    cnt[i] = counter.count(K)

print(max(cnt))