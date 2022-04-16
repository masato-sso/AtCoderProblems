
S = input()

ans = -1
for i in range(0,10):
    if(str(i) in S):
        continue
    ans = i
    break

print(ans)