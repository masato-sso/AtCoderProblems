
S = input()

# duplicate check
tmpS = "".join(list(set(S)))
if(len(tmpS) != len(S)):
    print("No")
    exit(0)

ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alpha = list("abcdefghijklmnopqrstuvwxyz")

cnt = 0
for Alpha in ALPHA:
    if(Alpha in S):
        cnt += 1

if(cnt == 0):
    print("No")
    exit(0)

cnt = 0
for Alpha in alpha:
    if(Alpha in S):
        cnt += 1

if(cnt == 0):
    print("No")
    exit(0)

print("Yes")