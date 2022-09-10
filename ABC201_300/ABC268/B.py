
S = input()
T = input()

flag = True
s_length = len(S)
t_length = len(T)
if(t_length < s_length):
    print("No")
    exit(0)
for i in range(len(S)):
    s = S[i]
    t = T[i]
    if(s != t):
        flag = False
        break

if(flag):
    print("Yes")
else:
    print("No")