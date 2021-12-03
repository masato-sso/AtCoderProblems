
N = input()

intN = int(N)

ans = "AGC0"
if(42 <= intN):
    ans = ans + str(intN + 1)
elif(10 <= intN):
    ans = ans + str(intN)
else:
    ans = ans + "0" + N

print(ans)