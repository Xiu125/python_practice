t=float(input('請輸入溫度:'))
a=int(input('哪一種溫度轉換\n華氏 轉 攝氏:請輸入1\n攝氏 轉 華氏:請輸入2'))
if a==1:
    T=(t-32)*5/9
    print("華氏",t,"度為攝氏",round(T,1),"度")
elif a==2:
    T=t*9/5+32
    print("攝氏",t,"度為華氏",round(T,1),"度")
else:
    print("請重新選擇轉換的方式")