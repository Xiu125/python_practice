import random

a=int(input("請輸入1~99間的數字"))
b=random.randint(1,99)

while True:
    if a>b:
        a=int(input("太大了，請重新輸入數字:"))
    elif a<b:
        a=int(input("太小了，請重新輸入數字:"))
    else:
        print("答對了,正確數字為",b)
        break;
