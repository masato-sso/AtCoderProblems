
N = int(input())
H = list(map(int, input().split()))

max_h = -1
for i in range(N):
    h = H[i]
    if(max_h < h):
        max_h = h
    else:
        break

print(max_h)