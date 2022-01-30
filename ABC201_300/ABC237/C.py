
S = input()
reverseS = S[::-1]

endAcount = 0
for s in reverseS:
    if (s == "a"):
        endAcount+=1
        continue
    else:
        break

startAcount = 0
for s in S:
    if (s == "a"):
        startAcount+=1
        continue
    else:
        break

tartgetS = S
if (startAcount < endAcount):
    tartgetS = "a"*(endAcount - startAcount) + tartgetS

flag = True
for idx in range(len(tartgetS)):
    if (tartgetS[idx] == tartgetS[-1 - idx]):
        continue
    else:
        flag = False
        break

if (flag):
    print("Yes")
else:
    print("No")
