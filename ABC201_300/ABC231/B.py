import collections

N = int(input())
S = []
for i in range(N):
    S.append(input())

c = collections.Counter(S)

print(c.most_common()[0][0])