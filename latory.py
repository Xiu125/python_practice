#方法一:用list[],if...else判斷
# import random

# a=[]
# while len(a)<6:
#     b=random.randint(1,49)
#     if b not in a:
#         a.append(b) #增加陣列用append
# print(a)

#方法二:用集合set(),有「項目不會重複的」特性
import random

a=set()
while len(a)<6:
    b=random.randint(1,49)
    a.add(b) #增加集合用add
print(a)

#發法三:用random.sample
# import random
# a=random.sample(range(1,49),6)
# print(a)