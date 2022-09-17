
x = int(input())
res = [0]
for d in range(60):
    if(x&(1 << d)):
        for i in range(len(res)):
            res.append(res[i]|(1 << d))

result = sorted(res)
for r in result:
    print(r)