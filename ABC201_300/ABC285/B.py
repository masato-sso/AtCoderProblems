
N = int(input())
S = input()

for i in range(1,N):
    flag = True
    l = -1
    for idx in range(N-i):
        if(S[idx] != S[idx+i]):
            l = idx
            continue
        flag = False
        break
    print(l + 1)
