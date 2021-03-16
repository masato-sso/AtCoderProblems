
N=int(input())

mod=pow(10,9)+7

def pow_method(r,N):
    ans=1
    for i in range(N):
        ans=ans*r%mod
    return ans

calc=pow_method(9,N)+pow_method(9,N)-pow_method(8,N)
ans=pow_method(10,N)-calc
ans=ans%mod
ans=(ans+mod)%mod

print(ans)
