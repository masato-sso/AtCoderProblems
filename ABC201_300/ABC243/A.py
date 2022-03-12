
V,A,B,C = map(int, input().split())

cycle = [A, B, C]
answer = ["F", "M", "T"]
rem = V
idx = 0
while(True):
    idx = idx % 3
    if(rem < cycle[idx]):
        print(answer[idx])
        break
    rem = rem - cycle[idx]
    idx+=1
