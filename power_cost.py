import decimal

a=float(input("請輸入月電度數:"))
if 0<=a<201:
    print("本月電費級距 每度3.2元","\n本月應繳",round(decimal.Decimal(3.2*a),0),"元")
elif 201<=a<300:
    print("本月電費級距 每度3.4元","\n本月應繳",round(decimal.Decimal(3.4*a),0),"元")
else:
    print("本月電費級距 每度3.6元","\n本月應繳",round(decimal.Decimal(3.6*a),0),"元")

#學習筆記
# 1. if elif else如何運用
# 2. decimal模組中的Decimal
#   為了確保運算出來的數值，浮點數沒有誤差，希望不影響四捨五入的結果，將數值改成十進位方式呈現
# 3. round
#   現實繳費金額只有整數，取道小數點第0位