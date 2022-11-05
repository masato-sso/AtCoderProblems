
S = input()

ans = -1
for idx,s in enumerate(S):
    if(s == "a"):
        ans = idx + 1

print(ans)
