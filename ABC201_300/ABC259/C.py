
S = input()
T = input()

size_s = len(S)
size_t = len(T)
 
i = 0
j = 0

ansFlag = True
while(i < size_s and j < size_t):
    if(S[i] != T[j]):
        ansFlag = False
        break
 
    same = S[i]
    s_count = 0
    while(S[i] == same):
        i += 1
        s_count += 1
        if i >= size_s:
            break
 
    t_count = 0
    while(T[j] == same):
        j += 1
        t_count += 1
        if j >= size_t:
            break
 
    if(s_count > t_count):
        ansFlag = False
        break
 
    if(t_count >= 2 and s_count < 2):
        ansFlag = False
        break
 
if(i < size_s or j < size_t):
    print('No')
elif(ansFlag):
    print("Yes")
else:
    print('No')