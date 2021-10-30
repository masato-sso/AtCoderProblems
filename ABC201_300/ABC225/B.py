from collections import defaultdict

N = int(input())
A = []
B = []
tree = defaultdict(list)

for i in range(N-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

keys = list(tree.keys())

for key in keys:
    vals = tree[key]
    flag=False
    if(len(vals)==N-1):
        flag=True
        break

if(flag):
    print("Yes")
else:
    print("No")