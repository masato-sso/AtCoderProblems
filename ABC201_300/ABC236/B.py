import collections

N = int(input())
A = list(map(int, input().split()))
counter = collections.Counter(A)

print([i for i in A if counter[i] <= 3][0])