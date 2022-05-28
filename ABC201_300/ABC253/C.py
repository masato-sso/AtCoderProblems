
Q = int(input())

cntDict = {}
minVal = 10 ** 10
maxVal = -1
for i in range(Q):
    q = list(map(int, input().split()))
    queryNo = q[0]
    if(queryNo == 1):
        x = q[1]
        if(x in cntDict):
            cntDict[x] += 1
        else:
            cntDict[x] = 1
        if(x < minVal):
            minVal = x
        if(maxVal < x):
            maxVal = x
    elif(queryNo == 2):
        x = q[1]
        c = q[2]
        if(x in cntDict.keys()):
            if(c < cntDict[x]):
                count = c
            else:
                count = cntDict[x]
            cntDict[x] -= count
            if(cntDict[x] == 0):
                cntDict.pop(x)
                keys = list(cntDict.keys())
                if(len(keys) == 0):
                    maxVal = -1
                    minVal = 10 ** 10
                else:
                    if(x == minVal):
                        minVal = min(keys)
                    if(x == maxVal):
                        maxVal = max(keys)
            
    elif(queryNo == 3):
        print(maxVal - minVal)

""" 下記ではTLEにならない。
n = int(input())
 
d = {}
max_num = -1
min_num = 10**10
for i in range(n):
    q = list(map(int, input().split()))
    if q[0] == 1:
        if q[1] in d:
            d[q[1]] += 1
        else:
            d[q[1]] = 1
        if q[1] < min_num:
            min_num = q[1]
 
        if q[1] > max_num:
            max_num = q[1]
 
    elif q[0] == 2:
        if q[1] in d.keys():
            if d[q[1]] > q[2]:
                c = q[2]
            else:
                c = d[q[1]]
            d[q[1]] -= c
            if d[q[1]] == 0:
                d.pop(q[1])
                if len(d.keys())==0:
                    max_num = -1
                    min_num = 10**10
                else:
                    if q[1] == min_num:
                        min_num = min(d.keys())
 
                    if q[1] == max_num:
                        max_num = max(d.keys())
 
    elif q[0] == 3:
        print(max_num - min_num)
"""