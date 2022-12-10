
S = input()

ALPHAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if(len(S) != 8):
    print("No")
    exit(0)

if(not(S[0] in ALPHAS and S[7] in ALPHAS)):
    print("No")
    exit(0)

num = S[1:7]
exitFlag = False
try:
    n = int(num)
    if(n < 100000 or 999999 < n):
        print("No")
        exitFlag = True
except:
    if(not(exitFlag)):
        print("No")
        exit(0)

if(exitFlag):
    exit(0)

print("Yes")