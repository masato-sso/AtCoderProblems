
S = input()
T = input()

Slength = len(S)
Tlength = len(T)

ans = -1
for i in range(Tlength):
    if(Slength <= i):
        ans = (i + 1)
        break
    if(S[i] == T[i]):
        continue
    ans = (i + 1)
    break

print(ans)
