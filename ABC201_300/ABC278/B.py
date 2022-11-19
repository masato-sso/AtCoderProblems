
H, M = map(int, input().split())

times = []
for h in range(0, 24):
    hour = ""
    if(h < 10):
        hour += "0" + str(h)
    else:
        hour += str(h)
    for m in range(0, 60):
        t = hour
        if(m < 10):
            t += "0" + str(m)
        else:
            t += str(m)
        times.append(t)

targetStr = ""
if(H < 10):
    targetStr = "0" + str(H)
else:
    targetStr = str(H)
if(M < 10):
    targetStr += "0" + str(M)
else:
    targetStr += str(M)

copy_times = times
times.extend(copy_times)

ans = ""
findFlag = False
for i in range(0, len(times)):
    t = times[i]
    if(t == targetStr):
        findFlag = True
    if(not(findFlag)):
        continue
    misTime = t[0] + t[2] + t[1] +t[3]
    if(misTime in times):
        ans = t
        break

print(ans[0] + ans[1] + " " + ans[2] + ans[3])