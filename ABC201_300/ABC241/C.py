
N = int(input())
S = []

for i in range(N):
    S.append(input())

cnt = 0
flag = False
for i in range(N):
    for j in range(N):
        if( (i + 5) < N):
            cnt = 0
            for k in range(6):
                if(S[i + k][j] == '#'):
                    cnt+=1
                if(cnt >= 4):
                    flag = True
        if( (j + 5) < N):
            cnt = 0
            for k in range(6):
                if(S[i][j + k] == '#'):
                    cnt+=1
                if(cnt >= 4):
                    flag = True
        if( ((i + 5) < N) and ((j + 5) < N)):
            cnt = 0
            for k in range(6):
                if(S[i + k][j + k] == '#'):
                    cnt+=1
                if(cnt >= 4):
                    flag = True
        if( ((0 <= (i - 5))) and ((j + 5) < N)):
            cnt = 0
            for k in range(6):
                if(S[i - k][j + k] == '#'):
                    cnt+=1
                if(cnt >= 4):
                    flag = True
        
if(flag):
    print("Yes")
else:
    print("No")