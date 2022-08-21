
X, Y, N = map(int, input().split())

ans1 = int(N/3)*Y + (N%3)*X
ans2 = int(N)*X

if(ans1 < ans2):
    print(ans1)
else:
    print(ans2)