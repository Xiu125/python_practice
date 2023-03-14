#階層為基數等腰三角形
# n=11
# star="*"
# space=" "

# for i in range(1,n+1,2):
#     print(int((n-i)/2)*" ",i*"*")

#置中三角形

n=2

for i in range(1,n*2+1,2):
    a=int((n*2-i-1)*0.5)
    print(" "*a,end="")
    for j in range(1,i+1,1):
        if j%2==0:
            print(" ",end="")
        else:
            print("*",end="")
    print("")


    
