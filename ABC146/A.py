
S=input()

day=["SUN","MON","TUE","WED","THU","FRI","SAT"]

idx=0
for i in range(len(day)):

    if S==day[i]:
        idx=i

print(7-idx)
