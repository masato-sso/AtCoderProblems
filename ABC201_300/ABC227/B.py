
N = int(input())
S = list(map(int,input().split()))

cnt = 0
for s in S:
    flag = False
    for a in range(1,s):
        for b in range(1,s):
            calc = 4*a*b + 3*a + 3*b
            if(calc == s):
                flag = True
                break
        if(flag):
            cnt += 1
            break

print(N - cnt)
