S = input()
a,b = map(int, input().split())

a = a - 1
b = b - 1

stringS = list(S)
ans = []
for idx,s in enumerate(stringS):
    if(idx == a):
        ans.append(stringS[b])
    elif(idx == b):
        ans.append(stringS[a])
    else:
        ans.append(stringS[idx])

print("".join(ans))