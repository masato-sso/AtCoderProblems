I=input()
s=I.split()
A=int(s[0])
B=int(s[1])

M=(A+B)/2.0

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

if(is_integer_num(M)):
    print(int(M))
else:
    print("IMPOSSIBLE")
