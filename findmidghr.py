# text=input("請輸入字串:")
# length=len(text)

# if length%2==0:
#     a=int(length/2)
#     print(text[a-1],text[a])
# else:
#     b=int((length-1)/2)
#     print(text[b])

import math

text=input("請輸入字串:")
length=len(text)
center=math.floor(length/2)

if length%2==0:
    print(text[center-1],text[center])
else:
    print(text[center])


