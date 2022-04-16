
A, B, K = map(int, input().split())

a = A
b = B
ans = 0
while(True):
    if(b <= a):
        break
    a = a * K
    ans += 1

print(ans)