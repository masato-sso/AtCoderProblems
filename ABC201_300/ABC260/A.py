from collections import Counter

S = input()

listS = list(S)

c = Counter(listS)

dic = dict(c.items())

keys = list(dic.keys())

ans = ""
for key in keys:
    cnt = dic[key]
    if(cnt == 1):
        ans = key

if(len(ans) == 0):
    ans = -1

print(ans)

