
n = int(input())
a = list(map(int, input().split()))
 
r = [i*i for i in a]
 
print(n * sum(r) - sum(a)**2)
