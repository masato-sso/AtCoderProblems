
N = int(input())
A = list(map(int, input().split()))

evens = []
odds = []
for a in A:
    if(a%2 == 0):
        evens.append(a)
    else:
        odds.append(a)
sortedEven = sorted(evens)[::-1]
sortedOdd = sorted(odds)[::-1]

maxEven = -1
if(2<=len(sortedEven)):
    maxEven = sortedEven[0] + sortedEven[1]
maxOdd = -1
if(2<=len(sortedOdd)):
    maxOdd = sortedOdd[0] + sortedOdd[1]

ans = -1
if(maxEven == -1 and maxOdd == -1):
    print(ans)
else:
    ans = max(maxEven, maxOdd)
    print(ans)