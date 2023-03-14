#羅馬數字轉阿拉伯數字
table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
roam=list(input("請輸入一組羅馬數字:"))
r=roam[::-1] #反轉陣列
output=table[r[0]]
for i in range(1,len(r)):
    if table[r[i]]<table[r[i-1]]:
        output=output-table[r[i]]
    else:
        output=output+table[r[i]]
print(output)   

