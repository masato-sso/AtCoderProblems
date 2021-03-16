import numpy as np

X=int(input())

#エラトステネスの篩
def get_next_primenumber(number):
    x=number
    number=number*2
    prime_list = []
    search_list = list(range(2,number+1))
    answer=2
    while True:
      if search_list[0] > np.sqrt(number):
        prime_list.extend(search_list)
        break
      else:
        head_num = search_list[0]
        prime_list.append(head_num)
        search_list.pop(0)
        search_list = [num for num in search_list if num % head_num != 0]
    
    plist=prime_list[::-1]
    for i in range(1,len(plist)):
        if(x>plist[i]):
            answer=plist[i-1]
            break

    return answer


print(get_next_primenumber(X))