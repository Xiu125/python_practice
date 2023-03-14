import datetime

BD=input("出生年月日(YYYY/MM/DD):")
BD_list=BD.split("/")
today=datetime.date.today()
y=today.year- int(BD_list[0])
m=today.month- int(BD_list[1])
d=today.day- int(BD_list[2])
if d<0:
    m=m-1
    if m<0:
        y=y-1
        m=m+12
        while :
    
    mDays=[31,28,31,30,31,30,31,31,30,31,30,31]
    d=int(mDays[int(BD_list[1])-1])+d
if m<0:
    y=y-1
    m=m+12
    d=d
print(y,"歲",m,"月",d,"天")


    

