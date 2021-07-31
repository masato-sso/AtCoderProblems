
X=input()

def check(X):
    for i in range(3):
        if(int(X[i+1])!=(int(X[i])+1)%10):
            return False
    return True

ans="Strong"
if(X.count(X[0])==4):
    ans="Weak"
if(check(X)):
    ans="Weak"

print(ans)