from collections import defaultdict

A, B, C, D, E = map(int, input().split())

d = defaultdict(int)

inList = [A, B, C, D, E]
for key in inList:
    d[key] += 1

d_keys = list(d.keys())
num_keys = len(d_keys)
if(num_keys == 2):
    if(d[d_keys[0]] == 3 and d[d_keys[1]] == 2):
        print("Yes")
    elif(d[d_keys[0]] == 2 and d[d_keys[1]] == 3):
        print("Yes")
    else:
        print("No")
else:
    print("No")