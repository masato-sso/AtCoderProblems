
N=int(input())
S=[]

for i in range(N):
    S.append(input())

print("AC x {}".format(S.count("AC")))
print("WA x {}".format(S.count("WA")))
print("TLE x {}".format(S.count("TLE")))
print("RE x {}".format(S.count("RE")))
