
N = int(input())
S = []
for i in range(N):
    S.append(input())

tmplen = len(list(set(S)))
if(tmplen != len(S)):
    print("No")
    exit(0)

for s in S:
    if(not(s[0] in ["H", "D", "C", "S"])):
        print("No")
        exit(0)
    if(not(s[1] in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"])):
        print("No")
        exit(0)

print("Yes")