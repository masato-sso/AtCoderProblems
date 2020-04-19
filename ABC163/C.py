import collections

N=int(input())

A=input().split()

c=collections.Counter(A)
result=[]

for i in range(1,N+1):
    result.append(c[str(i)])

for r in result:
    print(r)
