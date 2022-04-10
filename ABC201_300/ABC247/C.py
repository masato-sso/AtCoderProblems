
N = int(input())

def S(n):
    if(n == 1):
        return "1"
    s = S(n - 1)
    return "{} {} {}".format(s, n, s)

print(S(N))