
A, B = map(int, input().split())

ans = 0
prob = []
if(A == 1 or B == 1):
    prob.append(1)
if(A == 2 or B == 2):
    prob.append(2)
if(A == 3 or B == 3):
    prob.append(1)
    prob.append(2)
if(A == 4 or B == 4):
    prob.append(4)
if(A == 5 or B == 5):
    prob.append(1)
    prob.append(4)
if(A == 6 or B == 6):
    prob.append(2)
    prob.append(4)
if(A == 7 or B == 7):
    prob.append(1)
    prob.append(2)
    prob.append(4)

prob = list(set(prob))
ans = sum(prob)

print(ans)