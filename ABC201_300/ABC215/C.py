import itertools

SK=input().split()
S=SK[0]
K=int(SK[1])

set_S=itertools.permutations(list(S))
set_S=list(set(set_S))
sorted_S=sorted(set_S)

print("".join(list(sorted_S[K-1])))
