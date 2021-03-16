
S=input()

cnt=0
max_cnt=0
for s in S:
    if(s=="R"):
        cnt+=1
    else:
        cnt=0
    if(max_cnt<cnt):
        max_cnt=cnt

print(max_cnt)