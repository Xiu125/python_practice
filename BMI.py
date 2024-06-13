H=float(input("請輸入身高(公尺):"))
W=float(input("請輸入體重(公斤):"))
BMI=round(W/(H**2),3)
if BMI>24:
    note="太胖了"
elif 24>=BMI>=18.5:
    note="剛好"
else:
    note="太瘦了"
print("你的BMI為",BMI,note)

