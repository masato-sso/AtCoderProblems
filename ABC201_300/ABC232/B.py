
S = input()
T = input()

alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]

start_idx = alpha.index(S[0])
target_idx = alpha.index(T[0])

diff_idx = target_idx - start_idx

ans = T[0]
for i in range(1, len(S)):
    string = S[i]
    idx = alpha.index(string)
    target = alpha[(idx + diff_idx)%len(alpha)]
    ans = ans + target

if(ans == T):
    print("Yes")
else:
    print("No")