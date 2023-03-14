#倒數計時
import time

n=10
for i in range(n,0,-1):
    print('\r倒數',i,'秒',end=" ")
    T=time.sleep(1)
print("\r時間到   ",end=" ")

#學習筆記
#\r為游標位置退回到本行開頭位置
#end=" "運算完不換行
#如果後一行無法完全覆蓋前一行文字，新增空格覆蓋原本「秒」的位置，以解決!

#進度條
# import time

# n=20
# for i in range(1,n+1,1):
#     line=i*"_"
#     space=(n-i)*" "
#     print("\r[",line,space,"]",i*5,"%",end="")
#     T=time.sleep(0.2)
# print("\rFinished!",25*" ")

