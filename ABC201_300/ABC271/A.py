
N = int(input())

div = int(N / 16)
mod = N % 16

ans = ""
if(div < 10):
    ans = ans + str(div)
else:
    if(div == 10):
        ans = ans + "A"
    elif(div == 11):
        ans = ans + "B"
    elif(div == 12):
        ans = ans + "C"
    elif(div == 13):
        ans = ans + "D"
    elif(div == 14):
        ans = ans + "E"
    elif(div == 15):
        ans = ans + "F"

if(mod < 10):
    ans = ans + str(mod)
else:
    if(mod == 10):
        ans = ans + "A"
    elif(mod == 11):
        ans = ans + "B"
    elif(mod == 12):
        ans = ans + "C"
    elif(mod == 13):
        ans = ans + "D"
    elif(mod == 14):
        ans = ans + "E"
    elif(mod == 15):
        ans = ans + "F"

print(ans)