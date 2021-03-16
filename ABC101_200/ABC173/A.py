
N=int(input())

calc=N%1000

if(calc==0):
    print(0)
else:
    print(1000-calc)