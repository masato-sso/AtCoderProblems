
N = int(input())
A = list(map(int, input().split()))

rotate = 0
angles = []
for i in A:
    angles.append(rotate)
    rotate += i
    rotate = rotate % 360

angles.append(rotate)
angles.append(360)
results = sorted(angles)

ans = -1
for i in range(N + 1):
    if(ans < results[i+1] - results[i]):
        ans = results[i+1] - results[i]

print(ans)