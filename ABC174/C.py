
K=int(input())

if(K%2==0 or K%5==0):
  print("-1")

else:
  ans = 1
  s = 7
  while True:
    if s%K==0:
      print(ans)
      break
    else:
      s=(s%K)*10+7
      ans += 1
    