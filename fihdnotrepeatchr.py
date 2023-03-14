a=str(input("請輸入英文字串/數字:"))
b=len(a)
print("你輸入了",a,"總共",b,"個字元")

repeat=[]
not_repeat=[]

for i in a:
    times=a.count(i,0,b)
    if times>1 and i not in repeat:
        repeat.append(i)
    if times==1 and i not in repeat:
        not_repeat.append(i)
print(repeat)
print(not_repeat)

