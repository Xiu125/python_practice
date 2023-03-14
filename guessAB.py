import random
import time
# a=str(input("請輸入不重複的四個數字:"))
answer=random.sample(range(0,10),k=4) #每個項目不會重複
print(answer)
a=b=n=0
num=0
t=time.time()
while a!=4:
    a=b=n=0
    num+=1
    user=list(input("請輸入四個不重複的數字:"))
    for i in user:
        if answer[n]==int(user[n]):
            a+=1
        else:
            if int(i) in answer:
                b+=1
        n+=1
    output = ','.join(user).replace(',','')
    print(output,":",a,"A",b,"B")
T=round(time.time()-t,1)
print("答對了,總共",num,"次，花了",T,"秒")
