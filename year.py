
a=int(input('請輸入西元年:'))

if a%4==0:
    if a%100!=0:
        if a%400==0:
            print(a,'年是閏年')
        else:
            print(a,"年是平年")
    else:
        print(a,"年是平年")
else:
    print(a,"年是平年")
