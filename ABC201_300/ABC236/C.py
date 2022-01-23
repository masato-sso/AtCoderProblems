import collections

N,M = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))
counter = collections.Counter(S + T)

for s in S:
    if(counter[s] == 2):
        print("Yes")
    else:
        print("No")
