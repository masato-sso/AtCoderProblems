
A, B, C, D, E, F = map(int, input().split())

MOD =  998244353

ABC = (A*B*C) % MOD
DEF = (D*E*F) % MOD

ans = ABC - DEF
ans = ans % MOD
print(ans)