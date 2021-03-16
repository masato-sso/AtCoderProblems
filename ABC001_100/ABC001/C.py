# ABC001 C

ans=input().split(" ")
ang=float(ans[0])/10.0
m=float(ans[1])

angle=[11.25,33.75,56.25,78.75,101.25,123.75,146.25,168.75,191.25,213.75,236.25,258.75,281.25,303.75,326.25,348.75]
lb=["NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]

result=""

for i in range(len(lb)):
    if angle[i]<=ang and ang<angle[i+1]:
        result+=lb[i]
        break

if len(result)==0:
    result+="N"

result+=" "
sp=m/60.0


if sp*10-round(sp,1)*10<0.05*10:
    sp=round(sp,1)
else:
    sp=round(sp+0.9,1)

speed=[0.0,0.3,1.6,3.4,5.5,8.0,10.8,13.9,17.2,20.8,24.5,28.5,32.7]
sp_lb=["0","1","2","3","4","5","6","7","8","9","10","11"]

for i in range(len(sp_lb)):
    if speed[i]*10<=sp*10 and sp*10<=speed[i+1]*10-0.1*10:
        result+=sp_lb[i]
        break
    if i==len(sp_lb)-1 and speed[i+1]*10<=sp*10:
        result+="12"

if "0" in result[-1] and " " in result[-2]:
    result=""
    result="C 0"

print(result)