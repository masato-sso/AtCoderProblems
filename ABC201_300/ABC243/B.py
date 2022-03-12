
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def getIndex(l, x):
    if x in l:
        return l.index(x)
    else:
        return -1

ans1 = 0
ans2 = 0
for aIdx,a in enumerate(A):
    bIdx = getIndex(B,a)
    if(bIdx == -1):
        continue
    if(aIdx == bIdx):
        ans1+=1
    else:
        ans2+=1

print(ans1)
print(ans2)